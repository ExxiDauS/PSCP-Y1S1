"""Math for IT"""
import math
def main(radian):
    'circle'
    print("Area: %.3f" %(math.pi*(radian)**2))
    print("Circumference: %.3f" %(2*math.pi*radian))
main(float(input()))
