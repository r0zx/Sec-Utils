import argparse
import asyncio

from .scanner import scan_ports
from .dirbrute import dirbrute
from .fuzzer import fuzz
from .hashid import identify_hash
from .mangler import mangle, write_output


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

    # HTTP Fuzzer
    fuz = sub.add_parser("fuzz", help="HTTP parameter/path fuzzing")
    fuz.add_argument("-u", "--url", required=True, help="Target URL containing FUZZ")
    fuz.add_argument("-w", "--wordlist", required=True)

    # Hash Identifier
    hid = sub.add_parser("hashid", help="Identify hash algorithm")
    hid.add_argument("-H", "--hash", required=True)

    # Wordlist Mangler
    man = sub.add_parser("mangle", help="Generate wordlist variations")
    man.add_argument("-w", "--wordlist", required=True)
    man.add_argument("-o", "--output", required=True)

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

    elif args.cmd == "fuzz":
        with open(args.wordlist, "r") as f:
            words = f.readlines()
        await fuzz(args.url, words)

    elif args.cmd == "hashid":
        identify_hash(args.hash)

    elif args.cmd == "mangle":
        with open(args.wordlist, "r") as f:
            words = f.readlines()
        results = mangle(words)
        write_output(results, args.output)


def run():
    asyncio.run(main())
