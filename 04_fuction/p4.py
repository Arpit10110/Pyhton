# Function Returning Multiple Values
# Problem: Create a function that returns both the sum and multiplication of a two number at same time.


def sum_mul(a, b):
    return [a+b,a*b]

a=5
b=2

print("multipication of a+b is ",sum_mul(a,b)[0])
print("multipication of aXb is ",sum_mul(a,b)[1])
