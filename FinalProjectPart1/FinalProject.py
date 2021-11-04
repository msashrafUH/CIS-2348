#Muhammad Sameer Ashraf 1763709

#Importing the necessary modules
import csv
#Import datetime that will be used in organizing by date
from datetime import datetime, date
#Below is a class that will import and output the full items list with the required annotations

class Fullinventory:
    def __init__(self, listitems):

        self.listitems = listitems  #the list that will hold the outputted full inventory list

    def fullinvent (self):
            #The defined function will create and output for the fullnventory file
            #It also ensures the information in the file are arranged in order
            #The item attributes appear in order
            #and one item is contained per row.
            with open("Fullnventory.csv",'w') as file:
                items = self.listitems

                keys = sorted(items.keys(), key=lambda n: items[n]['Manufacturername'])
                for item in keys:
                    id = item
                    Manufacturername = items[item]['Manufacturername']
                    Price = items
                    Service_date = items
                    Damaged = items
                    file.write("{},{},{},{},{}\n".format(id,Manufacturername,Price,Service_date,Damaged))

    def Itemtype(self):
            #The fuction below creates an output for each item type
            #The item type is in the file name
            #The items are sorted by item ID
            #Each row of the file contains the item ID, manufacturer name, price, service date and list if damaged
            items = self.listitems
            types = []
            keys = sorted(items.keys())
            for item in items:
                itemtype = items
                if itemtype not in types:
                    types.append(itemtype)
            for type in types:
                fname = "LaptopInventory.csv"
                with open('./'+fname,'w') as file:
                    for item in keys:
                        id = item
                        Manufacturername = items[item]["Manufacturername"]
                        price = items[item]["price"]
                        Service_date = items
                        damaged = items

                        if type == itemtype:
                            file.write('{},{},{},{},{}\n'.format(id, Manufacturername, price, Service_date, damaged))
    def Pastservicedateinventory(self):
            ''''''
            #The function will create an output for the items that are past service date by the time the program is executed
            #Each of the rows contains the ID, name of the manufacturer, type, price, the service date and if damaged
            #The order of the items is done from the oldest to the most recent
            ''''''
            items = self.listitems
            keys = sorted(items.keys(), key=lambda x:datetime.strptime(items[x]['Service_date'],"%m/%d/%Y").date(), reverse=True)
            with open("./PastServiceDateInventory.csv",'w') as file:
                for item in keys:
                    id = item
            id = items
            Manufacturername = items[item]["Manufacturername"]
            Itemtype = items
            price = items[item]["price"]
            Service_date = items[item]['Service_date']

            damaged = items
            today = datetime.now().date()
            DateofExpiration = datetime.strptime(Service_date, "%m/%d/%Y").date()
            Expired = DateofExpiration<today
            if Expired:
                file.write('{},{},{},{},{},{}\n'.format(id, Manufacturername, Itemtype, price, Service_date, damaged))

    def Damagedinventory(self):
        ''''''
        #The function will output all items that are damaged
        #The rows will contain ID, manufacturer name, item type, price and service date
        #Items will be displayed in the order from the most to the least expensive
        items = self.listitems
        keys = sorted(items.keys(), key=lambda x: items[x]["price"], reverse=True)
        with open("./DamagedInventory.csv","w") as file:
            for item in keys:
                id = items
                Manufacturername = items[item]["Manufacturername"]
                Itemtype = items
                price = items[item]["price"]
                Service_date = items
                damaged = items[item]["damaged"]
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, Manufacturername, Itemtype, price, Service_date))

if __name__ == '__main__':
    items = {}
    files = ['ManufacturerList.csv','PriceList(1).xls','ServiceDatesList(3).xls']
    for file in files:
        with open(file, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    man_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]["Manufacturername"] = man_name.strip()
                    items[item_id]["item_type"] = item_type.strip()
                    items[item_id]["damaged"] = damaged.strip()

                elif file == files[1]:
                    price = line[1]
                    items[item_id]["price"] = price

                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]["Service_date"] = service_date
    #Calling the Fullinvent function,Itemtype function, Pastservicedateinventory function
    # and Damagedinventory function using the class Fullinventory to display the various output files
    Finventory = Fullinventory(items)
    Finventory.fullinvent()
    Finventory.Itemtype()
    Finventory.Pastservicedateinventory()
    Finventory.Damagedinventory()
    # The code gets the various manufacturers in a list
    types = []
    Manufacturername = []
    for item in items:
        check_manufact = items[item]['Manufacturername']
        check_type = items[item]['item_type']
        if check_manufact not in Manufacturername:
            Manufacturername.append(check_manufact)
        if check_type not in types:
            types.append(check_type)

