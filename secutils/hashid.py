import re
from rich.console import Console

console = Console()

HASH_PATTERNS = {
    "MD5": r"^[a-fA-F0-9]{32}$",
    "SHA1": r"^[a-fA-F0-9]{40}$",
    "SHA256": r"^[a-fA-F0-9]{64}$",
    "SHA512": r"^[a-fA-F0-9]{128}$",
    "NTLM": r"^[a-fA-F0-9]{32}$",
    "MySQL 3.x": r"^[a-fA-F0-9]{16}$",
    "MySQL 4.x": r"^[a-fA-F0-9]{40}$",
    "bcrypt": r"^\$2[aby]\$.{56}$",
}

def identify_hash(h):
    matches = []
    for name, pattern in HASH_PATTERNS.items():
        if re.match(pattern, h):
            matches.append(name)

    if matches:
        for m in matches:
            console.print(f"[bold green]{m}[/bold green]")
    else:
        console.print("[bold red]Unknown or unsupported hash format[/bold red]")
