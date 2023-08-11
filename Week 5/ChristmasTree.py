"""ChristmasTree"""


def tree(leaf, log):
    "tree"
    space = leaf - 1
    space_log = leaf - 2
    leaf_ontree = 1
    for _ in range(leaf):
        print(" " * space, end="")
        print("*" * leaf_ontree)
        space -= 1
        leaf_ontree += 2
    for _ in range(log):
        print(" " * space_log, end="")
        print("---")


tree(int(input()), int(input()))
