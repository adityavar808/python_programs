#password validation
import time

password = "aditya"
attempts = 3

while attempts>0:
    user_password = input("\nEnter The Password : ")
    if user_password == password:
        print('Password is Correct.')
        print('You Login in', attempts,'attempts.')
        break
    else:
        print('Wrong Password. Try Again')
        attempts = attempts - 1
        print("You Left", attempts, "attempts.")

    if attempts <= 0:
        print('\n\nWaiting for Try Again ...')
        count = 10
        while count:
            time.sleep(.75)
            print(count, end = ' ')
            count = count - 1
        attempts = 3
