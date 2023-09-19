sec = int(input("Enter the Time in sec : "))

hours = sec // (60*60)
sec = sec % (60*60)
minu = sec // 60
sec = sec % 60

print(f"Time : {hours}:{minu}:{sec}") 
