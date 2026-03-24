from app.core.models import ProbeResult
from app.core.normalizer import normalize_probe_result


def run_infohash_probe(infohash: str) -> dict:
    """
    Placeholder implementation for infohash-based metadata probing.
    """
    mock_files = [
        {"path": "docs/report.pdf", "size": 245760, "type": "pdf"},
        {"path": "images/photo1.jpg", "size": 512000, "type": "image"},
    ]

    result = ProbeResult(
        status="not_implemented",
        input_type="infohash",
        value=infohash,
        adapter="bittorrent_probe",
        message="Metadata-only infohash probing is not implemented yet.",
        btih=infohash,
        metadata_only=True,
        files=mock_files,
        source="local-placeholder",
    )
    return normalize_probe_result(result)


def run_magnet_probe(magnet: str, btih: str | None = None) -> dict:
    """
    Placeholder implementation for magnet-based metadata probing.
    """
    mock_files = [
        {"path": "evidence/case-notes.txt", "size": 4096, "type": "text"},
        {"path": "media/archive.zip", "size": 1048576, "type": "archive"},
    ]

    result = ProbeResult(
        status="not_implemented",
        input_type="magnet",
        value=magnet,
        adapter="bittorrent_probe",
        message="Metadata-only magnet probing is not implemented yet.",
        btih=btih,
        metadata_only=True,
        files=mock_files,
        source="local-placeholder",
    )
    return normalize_probe_result(result)