while 1:
    try:
        a = int(input('Enter the number'))
        rec = 1/a
        print(rec)
        break
    except (ValueError, TypeError) as e:
        print("invalid user value", e)
    except ZeroDivisionError as e:
        print("Integer is not valid fro the operation")
    else:
        print("operation successfully completed")