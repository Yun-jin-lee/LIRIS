def print_route_decision(input_type: str, adapter_name: str, reason: str) -> None:
    print(f"[OK] Input type: {input_type}")
    print(f"[OK] Adapter selected: {adapter_name}")
    print(f"[INFO] Routing reason: {reason}")


def print_adapter_result(result: dict) -> None:
    print(f"[INFO] Adapter status: {result.get('status')}")
    print(f"[INFO] Adapter: {result.get('adapter')}")
    print(f"[INFO] Message: {result.get('message')}")

    if "value" in result:
        print(f"[OK] Value: {result.get('value')}")

    if result.get("btih"):
        print(f"[OK] Extracted btih: {result.get('btih')}")