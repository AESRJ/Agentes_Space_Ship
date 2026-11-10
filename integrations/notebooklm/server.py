"""Project adaptation of KnowingDoing's NotebookLM for Codex (MIT, 2026).

Uses the original FastMCP -> subprocess CLI architecture, with scoped, durable memory.
See LICENSE.knowingdoing and README.md in this directory.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
from mcp.server.fastmcp import FastMCP
import project_memory as memory

mcp = FastMCP('space_ship_memory')


@mcp.tool()
def memory_status() -> dict:
    """Verify access to the pinned project notebook and list its sources."""
    return memory.status()


@mcp.tool()
def memory_ask(question: str) -> dict:
    """Query project memory with source citations; verify against current Git documents."""
    return memory.ask(question)


@mcp.tool()
def memory_checkpoint(record_id: str, summary: str, evidence: str, next_steps: str,
                      kind: str = 'avance', status: str = 'propuesto') -> dict:
    """Save a local immutable checkpoint and sync it. Pending is NOT success.

    Use a unique lowercase ID per event. An identical retry is safe. Content status:
    propuesto, aceptado, implementado, verificado, bloqueado. Include approval evidence
    for accepted decisions. Never include credentials or unrelated personal data.
    """
    return memory.checkpoint(record_id, summary, evidence, next_steps, kind, status)


@mcp.tool()
def memory_sync() -> dict:
    """Retry durable session records, deduplicating by remote source title/content hash."""
    return memory.sync_all()


@mcp.tool()
def memory_publish_context() -> dict:
    """Publish a versioned snapshot of project docs. Coordinate one publisher at a time."""
    return memory.publish_context()


if __name__ == '__main__':
    mcp.run(transport='stdio')
