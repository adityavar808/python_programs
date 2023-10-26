first = int(input("Enter the First Number : "))
second = int(input("Enter the Second Number : "))
third = int(input("Enter the Third Number : "))

if first > second and first > third:
    print(f"{first} is greatest.")

elif second > first and second > third:
    print(f"{second} is greatest.")

else:
    print(f"{third} is greatest.")