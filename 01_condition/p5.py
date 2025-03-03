# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

pasword = input("Enter the password--> ")

lenpassowrd = len(pasword)
if(lenpassowrd<6):
    print("Weak password")
elif(lenpassowrd>=6 and lenpassowrd<10):
    print("Medium password")
elif(lenpassowrd>=10):
    print("Strong password")