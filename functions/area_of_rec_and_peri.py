def area(l,b):
    return l * b

def peri(l,b):
    return 2 * (l + b)

length = int(input("Enter the Length : "))
breadth = int(input("Enter the breadth : "))

area = area(length, breadth)
peri = peri(length, breadth)

print(f"The area of rectangle is {area}.")
print(f"The Perimeter of Rectangle is {peri}.")