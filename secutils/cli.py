import argparse
import asyncio

from .scanner import scan_ports
from .dirbrute import dirbrute


def parse_args():
    parser = argparse.ArgumentParser(prog="sec-utils")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # Port scanner
    scan = sub.add_parser("scan", help="Async port scan")
    scan.add_argument("-t", "--target", required=True)
    scan.add_argument("-p", "--ports", default="1-1024")

    # Directory brute forcing
    dirb = sub.add_parser("dirbrute", help="Directory brute forcing")
    dirb.add_argument("-u", "--url", required=True)
    dirb.add_argument("-w", "--wordlist", required=True)

    return parser.parse_args()


def normalize_ports(port_range):
    start, end = port_range.split("-")
    return range(int(start), int(end) + 1)


async def main():
    args = parse_args()

    if args.cmd == "scan":
        ports = normalize_ports(args.ports)
        await scan_ports(args.target, ports)

    elif args.cmd == "dirbrute":
        with open(args.wordlist, "r") as f:
            words = f.readlines()
        await dirbrute(args.url, words)


def run():
    asyncio.run(main())

