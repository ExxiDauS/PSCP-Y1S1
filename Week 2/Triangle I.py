"""Triangle I"""
def main():
    """Triangle I"""
    numa = float(input())
    numb = float(input())
    numc = float(input())
    if (numa**2 + numb**2)**0.5 == numc or (numa**2 + numc**2)**0.5 == numb \
or (numb**2 + numc**2)**0.5 == numa:
        print("Yes")
    else:
        print("No")
main()
