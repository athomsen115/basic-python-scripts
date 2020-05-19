#!/usr/bin/env python3.8

import os
import glob
import shutil
import json

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

#Get a list of receipts
#receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0

for path in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('/')[-1]
    destination = f"./processed/{name}"
    shutil.move(path, destination)
    print(f"moved '{path}' tp '{destination}'")

print("Receipt subtotal: $%.2f" % subtotal)
