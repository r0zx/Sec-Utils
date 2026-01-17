import aiohttp
import asyncio
from rich.console import Console

console = Console()

async def fuzz_url(session, url):
    try:
        async with session.get(url, timeout=4) as resp:
            return url, resp.status
    except:
        return url, None


async def fuzz(target_url, wordlist):
    console.print(f"[bold cyan]Starting fuzzing on:[/bold cyan] {target_url}")

    async with aiohttp.ClientSession() as session:
        tasks = []
        for word in wordlist:
            word = word.strip()
            fuzzed = target_url.replace("FUZZ", word)
            tasks.append(fuzz_url(session, fuzzed))

        results = await asyncio.gather(*tasks)

    for url, status in results:
        if status and status not in [404]:
            console.print(f"[bold green]{status}[/bold green] → {url}")

    console.print("[bold yellow]Fuzzing complete.[/bold yellow]")

