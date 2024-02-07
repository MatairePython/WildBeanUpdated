import sqlite3
def getdata():
    conn = sqlite3.connect("cafe.db")
    cursor = conn.cursor()
    sqlCommand = """
       CREATE TABLE if not exists mactbl
       (
       itemcode TEXT,
       descr  TEXT,
       qty    INTEGER,
       cost   INTEGER,
       primary key (itemcode)
       ) """
    cursor.execute(sqlCommand)
    conn.commit() #writes to the database
    print("Table Created ")
    conn.close()   

def buyitems():
    conn = sqlite3.connect("cafe.db")
    cursor = conn.cursor()
    more = True
    while more:
        item = input("Enter Item Code ")
        sqlCommand = "SELECT * FROM cafetbl where itemcode = '%s' " % (item)
        result = cursor.execute(sqlCommand)
        found = False
        for rec in result:
            if rec[0]!= "   ":
                qty = int(input("Enter Quantity "))
                total = 0
                total = qty * int(rec[3])
                print("Total is ", total)
                money = int(input("Enter Money "))
                change = money - total
                print("Money ", money)
                print("Change ", change)
                
                moredrink = input("More Drink? y / n ").lower()
                if moredrink == "n":
                    more = False
    conn.close()

#menu

choice = 0
while choice !=3:
    print("        Welcome to Wild Bean Cafe ")
    print()
    print("1       Add Drinks To The Menu ")
    print()
    print("2       Buy Drinks ")
    print()
    print("3       Exit ")
    print()
    choice = int(input("Enter Choice "))
    if choice == 1 :
        getdata()
    elif choice == 2:
        buyitems()
