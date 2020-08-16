
fileName = input("input file name to create or open a file :")
file = open(fileName, mode="w")
file.write("hello world")
file.close()