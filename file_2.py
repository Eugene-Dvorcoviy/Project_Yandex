import random

f = open("lines.txt", mode="rt").readlines()
if len(f) != 0:
    print(f[random.randrange(0, len(f))])