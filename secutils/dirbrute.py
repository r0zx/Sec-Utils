import aiohttp
import asyncio
from rich.console import Console

console = Console()

async def fetch(session, url):
    try:
        async with session.get(url, timeout=3) as response:
            if response.status in [200, 301, 302, 403]:
                return url, response.status
    except:
        return None

async def dirbrute(base_url, wordlist):
    console.print(f"[bold cyan]Starting directory brute force on:[/bold cyan] {base_url}")

    async with aiohttp.ClientSession() as session:
        tasks = []
        for word in wordlist:
            full = base_url.rstrip("/") + "/" + word.strip()
            tasks.append(fetch(session, full))

        results = await asyncio.gather(*tasks)

    for result in results:
        if result:
            url, status = result
            console.print(f"[bold green]{status}[/bold green] → {url}")

    console.print("[bold yellow]Bruteforce complete.[/bold yellow]")

