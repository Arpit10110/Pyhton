#Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.


n=int(input("Enter the n"))

sum=0

for i in range (n):
    if(i%2==0):
        sum+=i;

print("sum of even numbers up to a given number n is --> ",sum)