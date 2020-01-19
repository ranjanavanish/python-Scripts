from typing import Any, Union

file = "New_Item_Price.dat"
import pickle
from getpass import getpass


class Retail:
    def __init__(self, index, desc, units, price):
        self.__index = index
        self.__desc = desc
        self.__units = units
        self.__price = price

    def ret_index(self):
        return self.__index

    def ret_desc(self):
        return self.__desc

    def ret_desc_price(self):
        return "For " + self.__desc + "Total price is : " + self.__price * self.__units

    def ret_units(self):
        return self.__units

    def ret_price(self):
        return self.__price

    def __str__(self):
        return "Item : " + self.__index + \
               "\nDescription : " + self.__desc + \
               "\nUnits : " + str(self.__units) + \
               "\nPrice per units : " + str(self.__price)


def main():
    print("Who you are \
          \nAre you customer or shopkeeper \
          \nif you are customer Press 1 \
          \nIf you are shopkeeper Press 2")
    cus_cli = int(input(": "))
    # cus_shop()
    if cus_cli == 2:
        password = passwords()
        if password == '123asd':
            print("logged in as Shopkeeper ")
            # " Writing code to show to enter the data in retail"
            again = "y"
            while again.lower() == 'y':
                retail = file_load()  # will be used to show the items in the store and also to add the new items.
                show_all(retail)
                z = welcome()
                if z == 1:
                    add_item(retail)
                elif z == 2:
                    edit_item(retail)
                elif z == 3:
                    delete_item(retail)
                elif z == 4:
                    search_item(retail)
                else:
                    exit("You chosen to Quit" + \
                         "\n Have a great Day")
                save_retail(retail)
        else:
            print("Wrong Password ")
            pass
    else:
        retail = file_load()
        customer(retail)


def welcome():
    global s
    print("Will be used to add the items")
    again = 'y'
    while again.lower() == 'y':
        print("1)Adding new items")
        print("2) Editing Items")
        print("3)Delete the item")
        print("4)Search Items ")
        print("5)Quit")

        try:
            s = int(input(":"))
            if s not in range(1, 6):
                again = 'n'  # killing outer again
                welcome()  # Starting inner again
            else:
                again = 'n'  # killing while loop if we have desired value
        except:
            print("Please Enter write value")
            print()
            again = "n"
            welcome()
    return s


def passwords():
    print("Password for Shopkeeper ")
    password = getpass(prompt="Password :")
    return (password)


def save_retail(retail):
    """Saving items in file after operations """
    outline = open(file, "wb")
    pickle.dump(retail, outline)
    outline.close()
    return


def file_load():  # will be used to show the items in the store and also to add the new items.
    try:
        inline = open(file, "rb")
        retail_data = pickle.load(inline)
        inline.close()
    except FileNotFoundError:
        retail_data = dict()
    return retail_data


def add_item(retail):
    print("You have chosen to enter the Retails infos..")
    index = input("Enter the Index Number ")
    if index not in retail:
        desc = input("Enter the item name : ")
        units = int(input("Total  units : "))
        price = int(input("Price of each unit : "))
        obc = Retail(index, desc, units, price)
        retail[index] = obc
        print("Item saved ...")
    else:
        print("Index already exist")


def edit_item(retail):
    print("Here you are on Edit page.. ")
    i = input("Enter the Index number you want to edit : ")
    if i in retail:
        print("you are going to edit values of : ", retail.get(i))
        s = retail.get(i)
        index = s.ret_index()
        name = s.ret_desc()
        price = s.ret_price()
        units = s.ret_units()
        # print("What you want to edit for %s" %name)
        ed_option = edits(name)
        if ed_option == 1:
            """Price Edition """
            new_price = int(input("New Price : "))
            obc = Retail(index, name, units, new_price)
            retail[index] = obc
        else:
            """Units Modification """
            new_units = int(input("New Units : "))
            obc = Retail(index, name, new_units, price)
            retail[index] = obc


def edits(name):  # ## for getting options for editing function
    global edit_value
    print("What you want to edit for %s : " % name)
    print("1)Price : ")
    print("2) Units ")
    try:
        edit_value = int(input(": "))
        again = 'y'
        while again.lower() == 'y':
            if edit_value not in range(1, 3):
                again = 'n'
                edits(name)
            else:
                again = 'no'
    except:
        again = "n"
        edits(name)
    return edit_value


def search_item(retail):
    print("Here you are on search page..")
    i = input("Enter the index number : ")
    if i in retail:
        print(retail.get(i))
    else:
        print("Index does not exist ")
    return


def delete_item(retail):
    i = input("Enter the index number you want to delete : ")
    if i in retail:
        del retail[i]
    else:
        print("Print it is not found")


def show_all(retail):
    s = retail.keys()

    list1 = list(s)
    # list1 = list1.sort()
    # print(type(list1))
    list1.sort()
    print("--------------------------------------------- ")
    print("|INDEX |  Description | Price | Units  |   ")
    for i in list1:
        z = retail.get(i)
        index = z.ret_index()
        des = z.ret_desc()
        price = z.ret_price()
        unit = z.ret_units()

        print("|", index, "|", des, " | ", price, " | ", unit, " | ")
    print("----------------------------------------------")


def customer(retail):
    print("Welcome Customer .. \
          \nHappy to see you...\
          \nPlease choose from following itesm")
    z = cuttomer_show_all(retail)
    print("Thanks for shopping")
    input("Enter to finish")


def cuttomer_show_all(retail):
    global descs, qty_price, qnty
    price_value = list()
    total = 0
    nub = 0
    print("What you want to buy:  ")
    list1 = retail.keys()
    list1 = list(list1)
    list1.sort()
    print("-----------------------------------------")
    print("Item      |    Name  |    Price Per Unit ")
    for i in list1:
        s = retail.get(i)
        index = s.ret_index()
        name = s.ret_desc()
        price = s.ret_price()
        print(index, "|", name, "|", price)
        nub += 1
    print("-----------------------------------------")
    again = 'y'
    while again.lower() == 'y':
        try:
            descs = int(input("What you want to buy : "))
            if descs not in range(1, nub + 1):
                print("Choice Wrong ...")
                again = 'n'
                cuttomer_show_all(retail)
            else:
                pass
        except:
            again = 'n'
            cuttomer_show_all(retail)
        count = False
        while count == False:
            qnty = input("How much you want to buy : ")
            if qnty.isdigit():
                qnty = int(qnty)
                count = True

        #price = descs * qnty
        #print(descs)
        descs = str(descs)
        if descs in retail:
            qty_s = retail.get(descs)
            qty_des = qty_s.ret_desc()
            #print(qty_s)
            qty_price = qty_s.ret_price()
            print("You chosen to buy %s which has price %s" %(qty_des, qty_price))
            price_qty = qnty * int(qty_price)
            price_value.append(price_qty)

        #price_unit = int(qttprice)*int(descs)
        #print("You selected total %d items and price is %d" % (int(descs), int(qttprice)*int(descs)))
        #total = total + price_unit
        again = input("Again  : ")

    for i in price_value:
        total = i + total
    print("Please pay total", total)



main()
