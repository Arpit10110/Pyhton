#  Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), E (below 60).

marks = int(input("Enter the marks--> "))

if(marks>=90 and marks<=100 ):
    print("You got grade A")

elif(marks>=80 and marks<=89 ):
    print("You got grade B")
    
elif(marks>=70 and marks<=79 ):
    print("You got grade C")

elif(marks>=60 and marks<=69 ):
    print("You got grade D")

elif( marks<60 ):
    print("You got grade E")