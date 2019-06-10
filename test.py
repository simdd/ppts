import os
import sys

print(sys.argv[1])

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, sys.argv[1])

with open(filename, 'r') as file:
    text = file.read()

print(text)
