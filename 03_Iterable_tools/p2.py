list = [1,2,5,7,8,"Arpit","Aman",5.2]

I = iter(list)

try:
   print(I)  # this I store the first address in the list 
   print(I.__next__()) #using this we can create a pointer which can easily iterate over the list but the value of the I will be same
   print(I.__next__()) #using this we can create a pointer which can easily iterate over the list but the value of the I will be same
   print(I.__next__()) #using this we can create a pointer which can easily iterate over the list but the value of the I will be same
except NameError:
    print(NameError)