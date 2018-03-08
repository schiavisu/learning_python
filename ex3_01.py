
hrs = input("Enter Hours:") #ask for the hours
rate = input("Enter Rate:") #ask for the rate per hour
h = float(hrs)
r = float(rate)
if h > 40.0 :
    pay = (40*r) + (h-40)*(r*1.5)
else :
    pay = h*r
print(pay)
