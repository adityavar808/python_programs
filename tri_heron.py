a = eval(input("Enter the first side : "))
b = eval(input("Enter the second side : "))
c = eval(input("Enter the third side : "))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5

print("Area of Triangle ",area)


