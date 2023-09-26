num = int(input("Enter the Number : "))

i = 1
while i <= 10:
    print(f'{num:<4} X {i:>2} = {num * i:4}')
    i = i + 1
