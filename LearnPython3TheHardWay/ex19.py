globalVar = "I am global"
def printTwo(first, second):
    print(f"first is {first}")
    print(f"second is {second}")
    print(f"{globalVar}")


printTwo(1, 2)
printTwo("abc", "def")