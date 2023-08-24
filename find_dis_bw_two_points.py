#import section
import math

#input section
x1 = int(input("Enter the first x-coordinate : "))
x2 = int(input("Enter the second x-coordinate : "))
y1 = int(input("Enter the first y-coordinate : "))
y2 = int(input("Enter the second y-coordinate : "))

#logic section
dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#display section
print("The distance between two points is ",dis)
