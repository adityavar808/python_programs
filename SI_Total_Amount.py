#input section
prin = int(input("Enter the Principal : "))
rate = int(input("Enter the rate : "))
time = int(input("Enter the Time : "))

#logic section
si = (prin*rate*time)/100
amount = prin + si

#display section
print("The simple Interest is ",si)
print("The Total Amount is ",amount)
