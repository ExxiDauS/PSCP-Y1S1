"""Largest Number"""
def main():
    """LargestNumber"""
    numa = input()
    numb = input()
    numc = input()
    sumval = biggest(numa+numb+numc, numa+numc+numb)
    sumval = biggest(sumval, numb+numa+numc)
    sumval = biggest(sumval, numb+numc+numa)
    sumval = biggest(sumval, numc+numb+numa)
    sumval = biggest(sumval, numc+numa+numb)
    print(int(sumval))
def biggest(val1, val2):
    """Biggest"""
    if val1 > val2:
        return val1
    return val2
main()
