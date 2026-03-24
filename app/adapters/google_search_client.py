from app.core.query_builder import build_google_query, build_google_search_url
from app.core.search_models import SearchRequest, SearchResult


def run_google_search(request: SearchRequest) -> dict:
    query = build_google_query(request)
    result = SearchResult(
        status="manual_or_pending",
        provider="google",
        adapter="google_search_client",
        use_case=request.use_case,
        query=query,
        manual_search_url=build_google_search_url(query),
        message="Google provider prepared a manual search URL. Live API integration is not configured.",
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