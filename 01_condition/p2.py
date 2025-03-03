# Movie Ticket Pricing
# # Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.


name=input("Enter the name--> ")
age=int(input("Ente the age--> "))
today_day = input("Enter the day--> ")

discount = 0;
ticket_price =0;

if(age>=12):
    ticket_price=12
else:
    ticket_price=8


if(today_day.lower()  =="wednessday" or today_day.lower()=="wed"):
    discount=2
    ticket_price -=discount 




print("--------------------------")
print("Customer Name-->{}".format(name))
print("Customer age-->{}".format(age))
print("Discount given-->${}".format(discount))
print("Ticket Price-->${}".format(ticket_price))
print("--------------------------")