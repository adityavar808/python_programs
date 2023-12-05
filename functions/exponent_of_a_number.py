def exponent(num, power):
    return num ** power

num = int(input("Enter the Number : "))
power = int(input("Enter the Power : "))

out = exponent(num, power)
print(f"The power of {num} raised to {power} is {out}.")