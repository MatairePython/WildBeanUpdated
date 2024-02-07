print("Welcome to Wild Bean Cafe")

def getdetails():
    wildbean = open("Wildbean.txt", "a")   
    num= int(input("Enter number of items"))
    for count in range(num):
        array = []
        code = int(input("Enter Item Code "))
        desc = input("Enter Coffee ")
        cost = int(input("Enter Cost "))
        quantity = int(input("Enter Quantity "))
        array.append(code)
        array.append(desc)
        array.append(cost)
        array.append(quantity)
        
        array = map(str, array)
        line =",".join(array)
        wildbean.writelines(line)  # Remove the 'line=' keyword argument
    wildbean.close()
        
def printall():
    wildbean = open("Wildbean.txt", "r")
    total_cost = 0
    for line in wildbean:
        fields = line.strip().split(",")
        if len(fields) == 4:
            code, desc, cost, quantity = map(int, fields)
            print("Item Code: ", code)
            print("Description: ", desc)
            print("Cost: ", cost)
            print("Quantity: ", quantity)
            total_cost += cost * quantity
    print("Total cost: ", total_cost)
    return total_cost

def search():
    wildbean = open("Wildbean.txt", "r")
    item_code = int(input("Enter item code to search: "))
    found = False
    for line in wildbean:
        fields = line.strip().split(",")
        if len(fields) == 4:
            code, desc, cost, quantity = map(int, fields)
            if code == item_code:
                print("Item Code: ", code)
                print("Description: ", desc)
                print("Cost: ", cost)
                print("Quantity: ", quantity)
                found = True
    if not found:
        print("Item not found!")
    wildbean.close()

def buy():
    total_cost = printall()
    money = int(input("Enter money: "))
    if money >= total_cost:
        print("Total cost: ", total_cost)
        print("Payment: ", money)
        change = money - total_cost
        print("Change: ", change)
    else:
        print("Not enough money!")

while True:
    print("\n1. Add drinks to the menu")
    print("2. Search for a drink")
    print("3. Buy drinks")
    print("4. Quit")
    option = int(input("Enter your option: "))
    if option == 1:
        getdetails()
    elif option == 2:
        search()
    elif option == 3:
        buy()
    elif option == 4:
        break
    else:
        print("Invalid option, try again!")
    
    
    
    
    