def modify_name(name): 
    name += " Mallya" 
    return name 

 

def modify_roll_number(roll_number): 
    roll_number += 1 
    return roll_number 

 

name = "Vijay" 
modified_name = modify_name(name) 
print("Original name:", name)
print("Modified name:", modified_name)

 

roll_number = 68
modified_roll_number = modify_roll_number(roll_number) 
print("Original roll number:", roll_number)
print("Modified roll number:", modified_roll_number)
