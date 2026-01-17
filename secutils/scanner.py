import asyncio
import socket
from rich.console import Console

console = Console()

async def check_port(host, port, timeout=1):
    try:
        conn = asyncio.open_connection(host, port)
        reader, writer = await asyncio.wait_for(conn, timeout=timeout)
        writer.close()
        await writer.wait_closed()
        return True
    except:
        return False

async def scan_ports(host, ports):
    console.print(f"[bold cyan]Scanning {host}...[/bold cyan]")
    tasks = [check_port(host, port) for port in ports]
    results = await asyncio.gather(*tasks)
    open_ports = [port for port, status in zip(ports, results) if status]
    
    for port in open_ports:
        console.print(f"[bold green]Open:[/bold green] {port}")
    
    if not open_ports:
        console.print("[bold red]No open ports found.[/bold red]")
