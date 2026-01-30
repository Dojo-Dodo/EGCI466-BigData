#!/usr/bin/env python3
import csv
import sys

reader = csv.reader(sys.stdin)
for index,row in enumerate(reader):
  if(index != 0):
    print(f"{row[17]}\n")