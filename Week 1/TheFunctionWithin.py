"""TheFunctionWithin"""

def funf(value):
    "Functionfx"
    funf1 = (2*value)
    return funf1
def fung(value):
    "Functiongx"
    fung1 = (3*(value**4))-(value**3)+(2*(value**2))+(10)
    return fung1
def funh(valuex, valuey, valuez):
    "functionhx"
    funh1 = ((valuez+valuex)**2)-(valuex*valuey)+(valuey**2)
    return funh1
def funi(valuea, valueb, valuec, valued):
    "functionix"
    funi1 = (valuea**2)+(valueb**2)-(valuec**2)
    funi2 = (valued**2)-(2*valuea*valued)+(2*valuea)
    return funi1/funi2
def main():
    """TheFunctionWithin"""
    numa = float(input())
    numb = float(input())
    numc = float(input())
    numd = float(input())
    pa1 = funh(funf(numa+numb), funf(numa-numc), fung(funf(numd**2)))
    pa2 = fung(funf(numa-numb))
    pa3 = funf(funf(funf(funf(funf(numc)))))
    pa4 = numd**8
    print(funf(funf(numa)))
    print(fung(funf(numa-numb)))
    print(funh(funf(numa+numb), funf(numa+numc), fung(funf(numd**2))))
    print(funi(pa1, pa2, pa3, pa4))
main()
