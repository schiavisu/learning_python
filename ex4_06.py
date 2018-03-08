def computepay(h,r):
    return (40*r) + (h-40)*(r*1.5)

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h>40 :
    p = computepay(h,r)
print(p)
