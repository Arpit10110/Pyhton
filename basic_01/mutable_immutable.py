# jiski value change ho jay usko mutable kahte hai

arr=[5,7,8,9,7]
narr=arr
print(arr)
print(arr)

arr[1]=91


# so here if change the value of the arr so it will effect the value of narr because array in  python is mutable
print(arr)
print(narr)

# jiski value change na ho  usko immutable kahte hai

a=5
b=a
print("value of a",a)
print("value of b",b)
print("value after change the value of a")
a=9
# so here if change the value of the a so it will not effect the value of b because int in  python is immutable 
print("value of a",a)
print("value of b",b)


#list of mutale in python
# list
# dict
# set



#list of immutale in python
# int
# float
# complex
# str
# tuple
# frozenset
# bool
# bytes