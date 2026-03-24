def tag_file(file_entry: dict) -> dict:
    path = (file_entry.get("path") or "").lower()
    file_type = (file_entry.get("type") or "").lower()

    tags: list[str] = []

    if file_type == "pdf":
        tags.extend(["document", "interesting"])
    elif file_type == "image":
        tags.append("image")
    elif file_type == "archive":
        tags.extend(["archive", "interesting"])
    elif file_type == "text":
        tags.extend(["text", "interesting"])

    if "report" in path or "evidence" in path or "case" in path:
        tags.append("high_value_candidate")

    if ".zip" in path or ".rar" in path or ".7z" in path:
        tags.append("compressed")

    score = 0
    if "interesting" in tags:
        score += 2
    if "high_value_candidate" in tags:
        score += 3
    if "compressed" in tags:
        score += 1

    tagged_entry = dict(file_entry)
    tagged_entry["tags"] = sorted(set(tags))
    tagged_entry["score"] = score
    return tagged_entry