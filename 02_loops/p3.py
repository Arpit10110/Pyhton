#  Reverse a String
# Problem: Reverse a string using a loop.


arr = input("Enter the string-->")

# we can also do it by using slice
# narr=arr[-1::-1]
# print(narr)

narr=""
arrlen = len(arr)-1

for i in range(arrlen,-1,-1):
    narr+=arr[i]

print("The reverse of string ",arr," is ",narr)