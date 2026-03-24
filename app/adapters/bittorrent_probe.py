from app.core.deduplicator import deduplicate_files
from app.core.models import ProbeResult
from app.core.normalizer import normalize_probe_result


def _filter_files(files: list[dict], filetype: str | None) -> list[dict]:
    if not filetype:
        return files
    return [file_entry for file_entry in files if file_entry.get("type") == filetype]


def run_infohash_probe(infohash: str, filetype: str | None = None) -> dict:
    """
    Placeholder implementation for infohash-based metadata probing.
    """
    mock_files = [
        {"path": "docs/report.pdf", "size": 245760, "type": "pdf"},
        {"path": "docs/report.pdf", "size": 245760, "type": "pdf"},
        {"path": "images/photo1.jpg", "size": 512000, "type": "image"},
    ]

    filtered_files = _filter_files(mock_files, filetype)
    deduplicated_files = deduplicate_files(filtered_files)

    result = ProbeResult(
        status="not_implemented",
        input_type="infohash",
        value=infohash,
        adapter="bittorrent_probe",
        message="Metadata-only infohash probing is not implemented yet.",
        btih=infohash,
        metadata_only=True,
        files=deduplicated_files,
        source="local-placeholder",
        extra={
            "filetype_filter": filetype,
            "deduplicated": True,
            "original_file_count": len(mock_files),
            "final_file_count": len(deduplicated_files),
        },
    )
    return normalize_probe_result(result)


def run_magnet_probe(magnet: str, btih: str | None = None, filetype: str | None = None) -> dict:
    """
    Placeholder implementation for magnet-based metadata probing.
    """
    mock_files = [
        {"path": "evidence/case-notes.txt", "size": 4096, "type": "text"},
        {"path": "evidence/case-notes.txt", "size": 4096, "type": "text"},
        {"path": "media/archive.zip", "size": 1048576, "type": "archive"},
    ]

    filtered_files = _filter_files(mock_files, filetype)
    deduplicated_files = deduplicate_files(filtered_files)

    result = ProbeResult(
        status="not_implemented",
        input_type="magnet",
        value=magnet,
        adapter="bittorrent_probe",
        message="Metadata-only magnet probing is not implemented yet.",
        btih=btih,
        metadata_only=True,
        files=deduplicated_files,
        source="local-placeholder",
        extra={
            "filetype_filter": filetype,
            "deduplicated": True,
            "original_file_count": len(mock_files),
            "final_file_count": len(deduplicated_files),
        },
    )
    return normalize_probe_result(result)