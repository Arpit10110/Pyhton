# Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a, b):
    if(type(a) == str and type(b)== str):
        return False
    else:
        return (a*b)

a=5
b=7
print(multiply(a, b))

d="Arpit"
f=2
print(multiply(d, f))


k="Arpit"
e="2"
print(multiply(k, e))