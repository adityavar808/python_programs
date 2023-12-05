def area(r):
    return 3.14 * r * r

def cir(r):
    return 2 * 3.14 * r

radius = int(input("Enter the Radius of Circle : "))

a = area(radius)
circumferance = cir(radius)

print(f"The Area of Circle is {a}.")
print(f"The Circumference of Circle is {circumferance}.")