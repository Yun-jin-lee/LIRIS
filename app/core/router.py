from dataclasses import dataclass


@dataclass
class RouteDecision:
    input_type: str
    adapter_name: str
    reason: str


def route_probe_input(*, infohash: str | None = None, magnet: str | None = None) -> RouteDecision:
    if infohash:
        return RouteDecision(
            input_type="infohash",
            adapter_name="bittorrent_probe",
            reason="Infohash input should be handled by the BitTorrent metadata probe adapter.",
        )

    if magnet:
        return RouteDecision(
            input_type="magnet",
            adapter_name="bittorrent_probe",
            reason="Magnet input should be handled by the BitTorrent metadata probe adapter.",
        )

    raise ValueError("No valid probe input was provided.")


def route_search_input(*, keyword: str) -> RouteDecision:
    if keyword.strip():
        return RouteDecision(
            input_type="keyword",
            adapter_name="jackett_client",
            reason="Keyword search should be routed to the Jackett adapter.",
        )

    raise ValueError("Keyword cannot be empty.")


def route_browse_input(*, target: str) -> RouteDecision:
    if target.strip():
        return RouteDecision(
            input_type="target",
            adapter_name="tor_lynx_client",
            reason="Text-based browsing targets should be routed to the Tor/Lynx adapter.",
        )

    raise ValueError("Browse target cannot be empty.")


def route_websearch_input(*, provider: str, keyword: str) -> RouteDecision:
    if not keyword.strip():
        raise ValueError("Web search keyword cannot be empty.")

    provider = provider.lower().strip()

    if provider == "google":
        return RouteDecision(
            input_type="websearch",
            adapter_name="google_search_client",
            reason="Google web search provider was selected.",
        )

    if provider == "yandex":
        return RouteDecision(
            input_type="websearch",
            adapter_name="yandex_search_client",
            reason="Yandex web search provider was selected.",
        )

    if provider == "baidu":
        return RouteDecision(
            input_type="websearch",
            adapter_name="baidu_search_client",
            reason="Baidu web search provider was selected.",
        )

    raise ValueError(f"Unsupported web search provider: {provider}")