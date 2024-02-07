passenger = int(input("Enter Number Of Adults: "))
children = int(input("Enter Number Of Children: "))
women = int(input("Enter Number Of Women: "))
adults = passenger - women  # calculate the number of adult men
passengers = passenger + children + women
bus = 0

# Conditions for bus types
if passenger < 20 and children < 5 and women < 5:
    bus = 1
elif passenger < 20 and children > 4 and women > 4:
    bus = 2
elif passenger > 19 and children < 5:
    bus = 3
elif passenger > 19 and children > 4:
    bus = 4
elif passenger > 19 and children > 4 and women > 4:
    bus = 5
else:
    print("Invalid")

adultcost = 0
childcost = 0

# Costs for each bus type
if bus == 1:
    adultcost = adults * 6
    childcost = children * 3.5
elif bus == 2:
    adultcost = adults * 6
    childcost = children * 3.5
elif bus == 3:
    adultcost = adults * 7
    childcost = children * 3.6
elif bus == 4:
    adultcost = adults * 8
    childcost = children * 3.2
elif bus == 5:
    adultcost = adults * 8
    childcost = children * 3.2

total = adultcost + childcost

print("Number Of Adults: ", adults)
print("Number Of Children: ", children)
print("Adult Fare: ", adultcost)
print("Child Fare: ", childcost)
print("Total: ", total)
print("Bus: ", bus)


        
        
        
        
    
    
