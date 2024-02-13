import re

fin = open("sha.txt", "r")

for line in fin:
    if re.search("96395e1", line):
        print(line)