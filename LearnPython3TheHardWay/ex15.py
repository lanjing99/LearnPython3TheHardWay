from sys import argv
# script, fileName = argv
print("input file name: ")
fileName = input()
print(f"your file name is {fileName}")
file = open(fileName)
content = file.read()
print(f"your content is {content}")
file.close()