from rich.console import Console

console = Console()

LEET_MAP = {
    "a": "4",
    "e": "3",
    "i": "1",
    "o": "0",
    "s": "5",
    "t": "7"
}

def leetify(word):
    out = ""
    for c in word:
        low = c.lower()
        out += LEET_MAP.get(low, c)
    return out


def mangle(words):
    results = []

    for w in words:
        w = w.strip()
        if not w:
            continue

        # Base variations
        results.append(w.lower())
        results.append(w.upper())
        results.append(w.capitalize())

        # Leetspeak
        results.append(leetify(w))

        # Appended numbers
        for i in range(1, 21):
            results.append(f"{w}{i}")

        # Symbols
        for sym in ["!", "@", "#", "$"]:
            results.append(f"{w}{sym}")

    return results


def write_output(results, output_file):
    with open(output_file, "w") as f:
        for r in results:
            f.write(r + "\n")

    console.print(f"[bold green]Generated {len(results)} mangled words → {output_file}[/bold green]")
