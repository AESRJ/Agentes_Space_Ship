[CmdletBinding()]
param(
    [string]$Destination = (Join-Path $env:USERPROFILE 'source\Agentes_Space_Ship'),
    [ValidateSet('HTTPS','SSH')][string]$Transport = 'HTTPS',
    [switch]$InstallPrerequisites,
    [switch]$Login,
    [string]$GitName,
    [string]$GitEmail
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Invoke-Checked {
    param([string]$Program, [string[]]$Arguments)
    & $Program @Arguments
    if ($LASTEXITCODE -ne 0) { throw "Command failed ($LASTEXITCODE): $Program" }
}

function Refresh-Path {
    $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')
}

function Install-Dependency {
    param([string]$Id)
    if (-not $InstallPrerequisites) {
        throw "Missing dependency $Id. Install it or rerun with -InstallPrerequisites."
    }
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        throw 'Install Windows App Installer (winget), Git and Python 3.11+ first.'
    }
    Invoke-Checked 'winget' @('install','--id',$Id,'--exact','--accept-source-agreements','--accept-package-agreements')
    Refresh-Path
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) { Install-Dependency 'Git.Git' }
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw 'Git was installed but is not visible yet. Open a new PowerShell and rerun.'
}
function Find-Python {
    foreach ($Candidate in @('py','python')) {
        $Command = Get-Command $Candidate -ErrorAction SilentlyContinue
        if (-not $Command) { continue }
        # The Microsoft Store alias is not a working Python installation.
        if ($Command.Source -match 'WindowsApps') { continue }
        $CandidateArgs = if ($Candidate -eq 'py') { @('-3') } else { @() }
        try {
            & $Candidate @CandidateArgs -c 'import sys; sys.exit(0 if sys.version_info >= (3,11) else 1)' 2>$null | Out-Null
            if ($LASTEXITCODE -eq 0) { return $Candidate }
        } catch { continue }
    }
    return $null
}

# HTTPS uses Git Credential Manager; SSH reuses a key already configured by the user.
$Remote = if ($Transport -eq 'SSH') { 'git@github.com:AESRJ/Agentes_Space_Ship.git' } else { 'https://github.com/AESRJ/Agentes_Space_Ship.git' }
if (Test-Path (Join-Path $PSScriptRoot '.git')) {
    $Repo = $PSScriptRoot
} else {
    $Repo = [IO.Path]::GetFullPath($Destination)
    if (-not (Test-Path $Repo)) {
        Invoke-Checked 'git' @('clone',$Remote,$Repo)
    } elseif (-not (Test-Path (Join-Path $Repo '.git'))) {
        throw "Destination exists and is not a Git repository: $Repo"
    }
}
$Origin = & git -C $Repo remote get-url origin
if ($LASTEXITCODE -ne 0 -or $Origin -notin @('git@github.com:AESRJ/Agentes_Space_Ship.git','https://github.com/AESRJ/Agentes_Space_Ship.git')) {
    throw 'Unexpected origin. No repository or remote was modified.'
}
Invoke-Checked 'git' @('-C',$Repo,'ls-remote','origin')
Invoke-Checked 'git' @('-C',$Repo,'config','--local','core.autocrlf','false')
if ($GitName) { Invoke-Checked 'git' @('-C',$Repo,'config','--local','user.name',$GitName) }
if ($GitEmail) { Invoke-Checked 'git' @('-C',$Repo,'config','--local','user.email',$GitEmail) }

$Venv = Join-Path $Repo '.venv'
$Python = Join-Path $Venv 'Scripts\python.exe'
if (-not (Test-Path $Python)) {
    $Launcher = Find-Python
    if (-not $Launcher) {
        Install-Dependency 'Python.Python.3.12'
        $Launcher = Find-Python
    }
    if (-not $Launcher) { throw 'Python 3.11+ is not visible yet. Open a new PowerShell and rerun.' }
    $Prefix = if ($Launcher -eq 'py') { @('-3') } else { @() }
    Invoke-Checked $Launcher ($Prefix + @('-c','import sys; assert sys.version_info >= (3,11), "Python 3.11+ required"'))
    Invoke-Checked $Launcher ($Prefix + @('-m','venv',$Venv))
}
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'
Invoke-Checked $Python @('-m','pip','install','-r',(Join-Path $Repo 'requirements.txt'))
Invoke-Checked $Python @((Join-Path $Repo 'scripts\configure_codex.py'),'--python',$Python)
Invoke-Checked $Python @((Join-Path $Repo 'scripts\validate.py'))
$Notebook = Join-Path $Venv 'Scripts\notebooklm.exe'
if ($Login) {
    Invoke-Checked $Python @('-m','playwright','install','chromium')
    Invoke-Checked $Notebook @('login')
}
# The scoped source list verifies account access; local auth-file existence is insufficient.
$env:NOTEBOOKLM_BIN = $Notebook
Invoke-Checked $Python @((Join-Path $Repo 'scripts\project_memory.py'),'status')
Write-Host "Ready: $Repo"
Write-Host 'Open this repository in Codex, trust it, and start a new session to load agents and space_ship_memory.'
Write-Host 'If NotebookLM access failed, request access from the owner and rerun with -Login.'
Write-Host 'No global Codex config, SSH keys or Google credentials were copied into the repository.'
