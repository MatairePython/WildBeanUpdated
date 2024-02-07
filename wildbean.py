def getdata():
    global pc, pt, cost, qty, pm
    more = True
    while more:
        print("Welcome To Wild Bean Cafe ")
        pc = input("Enter Item Code: ")
        pt = input("Enter Coffee type: ")
        cost = input("Enter Cost: ")
        while not cost.isdigit() or int(cost) > 20:
            print("Item should be less than £20 ")
            cost = input("Enter Cost: ")
        cost = int(cost)
        qty = int(input("Enter Quantity: "))
        pm = input("Payment Method: ").lower()
        while pm != "cash" and pm != "card" :
            print("Should be cash or card ")
            pm = input("Enter payment method: ")
        
        mi = input("More Items ? y/n ").lower()
        if mi == "n":
            more = False
        else:
            more = True
        
        
def process():
    global total, vat, cc, discount, money, change
    
    money = int(input("Enter Amount of money: "))
    
    change = 0
    nt = cost*qty
    
    if money < nt:
        print("Not enough Money ")
    else:
        change = money - nt
    
def printing():
    print("Product Desc: ", pc)
    print("Product Type: ", pt)
    print("Cost: ", cost)
    print("Quantity: ", qty)
    print("Payment Method: ", pm)
    print("Amount Paid: ", money)
    print("Change: ", change)

getdata()
process()
printing()
    