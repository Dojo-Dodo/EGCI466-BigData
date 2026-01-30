#!/usr/bin/env python3
import sys
import re
from collections import defaultdict

counts = defaultdict(int)

#with open("/content/drive/MyDrive/Big Data Project(Spotify)/demofile.txt", mode ='r')as file:

for line in sys.stdin:

  word = line.strip()

  cleanWord = word.replace("\\", "")

  try:
      mylist = eval(cleanWord)
  except Exception:
      mylist = [cleanWord]

  #Check some unstructure format
  final_artists = []
  for entry in mylist:
    pieces = re.split(r'[\/,-]', entry.strip())
    for p in pieces:
        cleaned = p.strip()
        if cleaned:
            final_artists.append(cleaned)

  #Separate all the artist
  for artist in final_artists:
    counts[artist] += 1

for artist, count in counts.items():
  print(f"{artist:60}{counts[artist]}")