a = 0
b = 1
n = int(input("enter number"))
""":wqif n==0:
     print(a)
elif n==1:
    print(a,b)
else:"""
print(a,b,end=" ")
i=1
while i<=n-2:
    c=a+b
    a=b
    b=c
    print(c,end =" ")
    i=i+1
