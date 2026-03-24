from app.core.query_builder import build_yandex_query, build_yandex_search_url
from app.core.search_models import SearchRequest, SearchResult


def run_yandex_search(request: SearchRequest) -> dict:
    query = build_yandex_query(request)
    result = SearchResult(
        status="manual_or_pending",
        provider="yandex",
        use_case=request.use_case,
        query=query,
        manual_search_url=build_yandex_search_url(query),
        message="Yandex provider prepared a manual search URL. Live API integration is not configured.",
        filters={
            "site": request.site,
            "filetype": request.filetype,
            "exact_phrase": request.exact_phrase,
            "exclude_terms": request.exclude_terms,
            "additional_terms": request.additional_terms,
            "language": request.language,
            "region": request.region,
        },
    )
    return result.__dict__