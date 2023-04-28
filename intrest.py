p = int(input("enter principle"))
r = int(input("enter rate"))
t = int(input("enter time"))
ci = p*(pow((1+r/100),t))
print("coumpound intrest is: {}".format(ci))
print("SImple intrest is : {}".format(p*t*r/100))

