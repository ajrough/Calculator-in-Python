print("CALCULATOR")
print("1.Addition")
print("2.Multiplication")
opt=int(input("Enter your choice :"))
if opt==1:
    print("Enter 2 number:")
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))
    print("The Sum is",a+b)
elif opt==2:
    print("Enter 2 number:")
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))
    print("The Product is",a*b)