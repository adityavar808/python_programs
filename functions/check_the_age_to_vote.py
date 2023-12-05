def vote(age):
    if age >= 18:
        return "You are Eligible."
    else:
        return "You are not Eligible."

age = int(input("Enter the Age : "))
out = vote(age)
print(out)