import os
import sys

origin_path = sys.argv[1]

for root, dirs, files in os.walk(origin_path):
	for file in files:
		if "Thumbs" in file:
			print(root)
