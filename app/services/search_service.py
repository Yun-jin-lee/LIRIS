from urllib.parse import quote_plus

import requests

from app.adapters.lynx_client import open_with_lynx
from app.config import load_config


def build_search_url(keyword: str, provider: str) -> str:
    query = quote_plus(keyword)
    provider = provider.lower()

    if provider == "ddg":
        return f"https://lite.duckduckgo.com/lite/?q={query}"

    if provider == "baidu":
        return f"https://www.baidu.com/s?wd={query}"

    raise ValueError("Direct URL building is only used for ddg and baidu.")


def get_serpapi_results(keyword: str, provider: str, max_results: int = 5) -> list[dict]:
    config = load_config()

    if not config.serpapi_api_key:
        raise ValueError("SERPAPI_API_KEY is not set in .env.")

    provider = provider.lower()

    if provider == "google":
        params = {
            "engine": "google",
            "q": keyword,
            "api_key": config.serpapi_api_key,
        }
    elif provider == "yandex":
        params = {
            "engine": "yandex",
            "text": keyword,
            "yandex_domain": "yandex.com",
            "lang": "en",
            "api_key": config.serpapi_api_key,
        }
    else:
        raise ValueError("SerpApi supports only google and yandex in this flow.")

    response = requests.get(
        "https://serpapi.com/search.json",
        params=params,
        timeout=20,
    )
    response.raise_for_status()

    data = response.json()
    organic_results = data.get("organic_results", [])

    cleaned_results = []
    for result in organic_results[:max_results]:
        title = result.get("title") or "<no title>"
        link = result.get("link")
        snippet = result.get("snippet") or ""

        if not link:
            continue

        cleaned_results.append(
            {
                "title": title,
                "link": link,
                "snippet": snippet,
            }
        )

    if not cleaned_results:
        raise RuntimeError(f"No usable {provider} results returned by SerpApi.")

    return cleaned_results


def choose_result(results: list[dict]) -> str:
    print()
    print("[OK] Search results")
    print()

    for idx, result in enumerate(results, start=1):
        print(f"[{idx}] {result['title']}")
        print(f"    {result['link']}")
        if result["snippet"]:
            print(f"    {result['snippet']}")
        print()

    while True:
        choice = input("Choose result number (or q to quit): ").strip().lower()

        if choice == "q":
            raise KeyboardInterrupt

        if not choice.isdigit():
            print("[ERROR] Please enter a number or q.")
            continue

        number = int(choice)
        if 1 <= number <= len(results):
            return results[number - 1]["link"]

        print(f"[ERROR] Choose a number between 1 and {len(results)}.")


def handle_search(user_input: str, provider: str = "ddg", dump: bool = False) -> int:
    provider = provider.lower()

    print("[OK] Keyword detected")
    print(f"[INFO] Provider: {provider}")
    print(f"[INFO] Search query: {user_input}")

    if provider in {"google", "yandex"}:
        print("[INFO] External provider selected through SerpApi.")
        print("[INFO] This may reduce privacy compared to the default provider.")

        results = get_serpapi_results(user_input, provider)
        target_url = choose_result(results)

        print()
        print(f"[INFO] Opening selected result: {target_url}")
        return open_with_lynx(target_url, dump=dump)

    search_url = build_search_url(user_input, provider)
    print(f"[INFO] Search URL: {search_url}")

    if provider != "ddg":
        print("[INFO] External provider selected.")
        print("[INFO] This may reduce privacy and may be blocked by the provider.")

    return open_with_lynx(search_url, dump=dump)