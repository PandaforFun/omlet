subjects = ["Mathematics", "Computer Science", "Physics", "Biology"] 

 

print("Favorite Subjects:") 
for subject in subjects: 
    print(subject) 

 

print("\nFavorite Subjects (excluding 'Physics'):") 
for subject in subjects: 
    if subject == "Physics": 
        continue 
    print(subject) 

 

print("\nFavorite Subjects (until 'Biology' is encountered):") 
for subject in subjects: 
    print(subject) 
    if subject == "Biology": 
        break 

 

print("\nNumbers:") 
for num in range(1, 11): 
    if num % 2 == 0: 
        continue 
    print(num) 
    if num > 5: 
        break 

 

def SayHi(name): 
    pass 

 

SayHi("Vijay Mallya") 

 

x = 10 
if x > 5: 
    print("x is greater than 5") 
else: 
    pass 

 
