from urllib.parse import quote_plus

from app.core.search_models import SearchRequest


def build_google_query(request: SearchRequest) -> str:
    parts: list[str] = []

    if request.keyword:
        parts.append(request.keyword)

    if request.exact_phrase:
        parts.append(f'"{request.exact_phrase}"')

    if request.site:
        parts.append(f"site:{request.site}")

    if request.filetype:
        parts.append(f"filetype:{request.filetype}")

    for term in request.additional_terms:
        parts.append(term)

    for term in request.exclude_terms:
        parts.append(f"-{term}")

    return " ".join(parts).strip()


def build_yandex_query(request: SearchRequest) -> str:
    parts: list[str] = []

    if request.keyword:
        parts.append(request.keyword)

    if request.exact_phrase:
        parts.append(f'"{request.exact_phrase}"')

    if request.site:
        parts.append(f"site:{request.site}")

    if request.filetype:
        parts.append(f"mime:{request.filetype}")

    for term in request.additional_terms:
        parts.append(term)

    for term in request.exclude_terms:
        parts.append(f"-{term}")

    return " ".join(parts).strip()


def build_baidu_query(request: SearchRequest) -> str:
    parts: list[str] = []

    if request.keyword:
        parts.append(request.keyword)

    if request.exact_phrase:
        parts.append(f'"{request.exact_phrase}"')

    if request.site:
        parts.append(f"site:{request.site}")

    if request.filetype:
        parts.append(f"filetype:{request.filetype}")

    for term in request.additional_terms:
        parts.append(term)

    for term in request.exclude_terms:
        parts.append(f"-{term}")

    return " ".join(parts).strip()


def build_google_search_url(query: str) -> str:
    return f"https://www.google.com/search?q={quote_plus(query)}"


def build_yandex_search_url(query: str) -> str:
    return f"https://yandex.com/search/?text={quote_plus(query)}"


def build_baidu_search_url(query: str) -> str:
    return f"https://www.baidu.com/s?wd={quote_plus(query)}"