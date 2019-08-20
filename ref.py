import os, sys

file = open("references", "r")
arr = []
for line in file:
    if line in arr:
        pass
    else:
        arr.append(line)
after = sorted(arr)
for element in after:
    print(element)