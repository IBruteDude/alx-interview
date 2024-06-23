#!/usr/bin/python3
""" Module for defining the log stats parser
"""
import signal
import sys
import re


itercount = 0
file_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats(*_) -> None:
    """ print the current stats
    """
    print(f"File size: {file_size}", flush=True)
    for code, count in sorted(status_codes.items(), key=lambda s: int(s[0])):
        if count:
            print(f"{code}: {count}", flush=True)
    global itercount
    itercount = 0

signal.signal(signal.SIGINT, print_stats)

for line in sys.stdin:
    itercount += 1
    if line is None:
        continue
    m = re.match(r"""(\d*.\d*.\d*.\d*) - \[(.*)\] \"GET /projects/260 HTTP/1.1\" (\d*) (\d*)""", line)
    if m is None:
        continue
    ipaddr, date, status_code, size = m.groups()
    if status_code in status_codes:
        status_codes[status_code] += 1
    file_size += int(size)
    if itercount == 10:
        print_stats()
        itercount = 0
