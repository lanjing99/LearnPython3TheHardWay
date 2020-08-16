from sys import argv
from os.path import exists

script, fromFileName, toFileName = argv
print(f"{script} copy file from {fromFileName} to {toFileName}")
fromFile = open(fromFileName)
fromFileData = fromFile.read()
fromFile.close()

print(f"{toFileName} exist? {exists(toFileName)}")

toFile = open(toFileName, mode="w")
toFile.write(fromFileData)
toFile.close()
