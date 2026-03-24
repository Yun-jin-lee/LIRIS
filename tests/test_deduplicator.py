from app.core.deduplicator import deduplicate_files


def test_deduplicate_files_removes_exact_duplicates():
    files = [
        {"path": "docs/report.pdf", "size": 100, "type": "pdf"},
        {"path": "docs/report.pdf", "size": 100, "type": "pdf"},
        {"path": "images/photo.jpg", "size": 200, "type": "image"},
    ]

    result = deduplicate_files(files)

    assert len(result) == 2
    assert result[0]["path"] == "docs/report.pdf"
    assert result[1]["path"] == "images/photo.jpg"


def test_deduplicate_files_keeps_distinct_entries():
    files = [
        {"path": "docs/report.pdf", "size": 100, "type": "pdf"},
        {"path": "docs/report.pdf", "size": 101, "type": "pdf"},
    ]

    result = deduplicate_files(files)

    assert len(result) == 2