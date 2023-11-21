# Write a python script to merge two python dictionaries

info1 = {"name" : "Aditya", 
         "mobile" : "**********",
         "roll_no." : 4,
         "college" : "GLA UNIVERSITY"}

print(info1)

new_info = {'name' : "Jatin Thakur",
            "cpi" : 9.5}

for i in new_info:
    info1[i] = new_info[i]

print(info1)