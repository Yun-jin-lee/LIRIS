import requests

from app.adapters.lynx_client import open_with_lynx
from app.config import load_config


PAGE_SIZE = 5


def get_searxng_results(keyword: str, provider: str = "all", page: int = 1) -> list[dict]:
    config = load_config()

    params = {
        "q": keyword,
        "format": "json",
        "pageno": page,
    }

    if provider != "all":
        params["engines"] = provider

    response = requests.get(
        f"{config.searxng_url}/search",
        params=params,
        timeout=20,
    )
    response.raise_for_status()

    data = response.json()
    raw_results = data.get("results", [])

    cleaned_results: list[dict] = []
    for item in raw_results[:PAGE_SIZE]:
        url = item.get("url")
        if not url:
            continue

        cleaned_results.append(
            {
                "title": item.get("title") or "<no title>",
                "link": url,
                "snippet": item.get("content") or "",
                "engine": item.get("engine") or "",
            }
        )

    return cleaned_results


def choose_searxng_result(keyword: str, provider: str) -> str:
    page = 1

    while True:
        results = get_searxng_results(keyword, provider=provider, page=page)

        if not results:
            if page == 1:
                raise RuntimeError(f"No usable results returned for provider '{provider}'.")
            print("[INFO] No more results.")
            page -= 1
            continue

        print()
        print(f"[OK] SearXNG results - page {page}")
        if provider != "all":
            print(f"[INFO] Engine filter: {provider}")
        print()

        for idx, result in enumerate(results, start=1):
            engine_label = f" [{result['engine']}]" if result["engine"] else ""
            print(f"[{idx}] {result['title']}{engine_label}")
            print(f"    {result['link']}")
            if result["snippet"]:
                print(f"    {result['snippet']}")
            print()

        print("Commands: 1-5=open, n=next page, p=previous page, q=quit")
        choice = input("Choose: ").strip().lower()

        if choice == "q":
            raise KeyboardInterrupt

        if choice == "n":
            page += 1
            continue

        if choice == "p":
            if page > 1:
                page -= 1
            else:
                print("[INFO] Already on the first page.")
            continue

        if choice.isdigit():
            number = int(choice)
            if 1 <= number <= len(results):
                return results[number - 1]["link"]

        print("[ERROR] Invalid choice.")


def handle_search(user_input: str, provider: str = "all", dump: bool = False) -> int:
    print("[OK] Keyword detected")
    print("[INFO] Provider: searxng")
    print(f"[INFO] Search query: {user_input}")
    if provider != "all":
        print(f"[INFO] Engine filter: {provider}")

    target_url = choose_searxng_result(user_input, provider)

    print()
    print(f"[INFO] Opening selected result: {target_url}")
    return open_with_lynx(target_url, dump=dump)