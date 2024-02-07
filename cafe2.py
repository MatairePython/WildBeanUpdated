

def getdata():
    global code, descr, qty, sp, cost, total, money, change
    
    cost = 0
    total = 0
    money=0
    change=0
  
    cafe = open("cafe.txt", "a")
    more = True
    while more :
        array = []
        code = input("Enter Code ")
        descr = input("Enter Description ")
        qty = int(input("Enter Quantity "))
        sp = input("Enter Selling Price ")
        array.append(code)
        array.append(descr)
        array.append(qty)
        array.append(sp)
        array = map(str, array)
        line = (",").join(array)
        cafe.writelines(line + "\n")
        moreitems = input("More Items? ").lower()
        if moreitems == "n":
            more = False

    cafe.close()
#getdata()
    
def readdata():
    cafe = open("cafe.txt", "r")
    for line in cafe:
        fields = line.split(",")
        print ("Code  ", fields[0], "Description ", fields[1], "Quantity ", fields[2], "Selling Price ", fields[3])
    cafe.close()
#readdata()


def finddata():
    cafe = open("cafe.txt", "r")
    name = input("Enter Item Code  ")
    found = False
    for line in cafe :
        fields = line.split(",")
        if name == fields[0]:
            print ("Item Found ")
            print ("Description  ", fields[0], "Code ", fields[1], "Quantity ", fields[2], "Selling Price ", fields[3])
            found = True
            
    if not found:
        print("Item Not Found ")
    cafe.close()
    
#finddata()
#Main Menu
    
def printdata():
    money = input("Enter Money ")
    total = cost*qty
    change = money - total
    print("Money: ", money)
    print("Total: ", total)
    print("Change: ", change)

choice = 0
while choice != 4 :
    print ("1 ... Enter Data ")
    print()
    print("2 ... Read Data ")
    print()
    print("3 ... Find Data ")
    print()
    print("4 ... Print Data ")
    choice = int(input("Enter Choice "))
    if choice == 1:
        getdata()
    elif choice == 2:
        readdata()
    elif choice == 3:
        finddata()
    elif choice == 4:
        printdata()

