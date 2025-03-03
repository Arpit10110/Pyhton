# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).


age = int(input("Enter the age group-->"))

if(age<13):
    print("You are a child")
elif(13<=age and age<=19 ):
    print("You are a Teenager")
elif(20<=age and age<=59):
    print("You are adult")
else:
    print("You are senior")
