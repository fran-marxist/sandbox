import sys

args = sys.argv
print(args)
total = 0
for x in range(1, len(args)):
    total = total + int(args[x])

print((total)/len(args))