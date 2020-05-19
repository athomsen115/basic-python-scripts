#!/usr/bin/env python3.8

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
args = parser.parse_args()


try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)
else:
    with f:
        lines = f.readlines()
        lines.reverse()
    
        if args.limit:
            lines = lines[:args.limit]

        for line in lines:
            print(line.strip()[::-1])
