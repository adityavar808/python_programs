str = input("Enter the String : ")
revstr = str[::-1]

if str == revstr:
    print(f'{str} is a palindrone.')

else:
    print(f'{str} is not a palindrone.')