def extract_action_items(text: str) -> list[str]:
    lines = [line.strip("- ") for line in text.splitlines() if line.strip()]
    results: list[str] = []

    keywords = ["todo", "action", "fix", "improve", "add", "implement", "refactor"]

    for line in lines:
        normalized = line.lower()

        # existing rules (tetap dipakai)
        if normalized.startswith("todo:") or normalized.startswith("action:"):
            results.append(line)
        elif line.endswith("!"):
            results.append(line)

        # new rule (tambahan)
        elif any(keyword in normalized for keyword in keywords):
            results.append(line)

    return results