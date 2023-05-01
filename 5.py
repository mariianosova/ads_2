import random

lines = open("lines.txt").readlines()
print(random.choice(lines).rstrip())
