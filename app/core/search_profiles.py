def apply_use_case(keyword: str, use_case: str | None) -> dict:
    """
    Return profile settings for a supported search use case.
    """
    base = {
        "keyword": keyword,
        "filetype": None,
        "exact_phrase": None,
        "exclude_terms": [],
        "additional_terms": [],
        "site": None,
    }

    if not use_case:
        return base

    use_case = use_case.lower()

    if use_case == "apk":
        base["filetype"] = "apk"
        base["additional_terms"] = ["download", "android"]
        return base

    if use_case == "documents":
        base["additional_terms"] = ["pdf", "doc", "report"]
        return base

    if use_case == "images":
        base["additional_terms"] = ["image", "photo"]
        return base

    if use_case == "leaks":
        base["additional_terms"] = ["paste", "dump", "database"]
        return base

    return base