"""Parallelogram"""
def main():
    """Parallelogram"""
    word = input()
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            print(" ", end="")
        for j in range(0, i+1):
            print(word[j], end="")
        print()
    for i in range(len(word)-1):
        print(word[i+1:len(word)])
    print()
main()
