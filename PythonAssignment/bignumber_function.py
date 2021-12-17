def Biggest(a,b,c):
    if a>b and a>c :
        print("Biggest Number=",a)
    elif b>a and b>c:
        print("Biggest Number=",b)
    else:
        print("Biggest Number=",c)
a = input("enter first number:")
b = input("enter second number:")
c = input("enter third number:")
result = Biggest(a,b,c)
print("largest is:",result)