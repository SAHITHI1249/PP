a = int(input("enter  an number"))
count=0
for i in range(2,a):
    if a%i==0:
        count =count+1
        break
if count==0:
    print("prime")
else:
    print("composite")
