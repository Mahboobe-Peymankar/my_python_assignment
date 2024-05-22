import qrcode
import prettytable

PRODUCTS = []

def read_from_database ():
    f = open ("database.txt","r")

    for line in f :
        
        result = line.split (",")
        edit_count = result [3]
        
        my_dict = {'code' : result [0] , 'name' : result [1] , 'price' : result [2], 'count' : edit_count.replace("\n","")}
        

        PRODUCTS.append (my_dict)
    print (PRODUCTS)
        

    f.close ()

def show_menu () :
    print ("1- Add")
    print ("2- Edit")
    print ("3- Remove")
    print ("4- Search")
    print ("5- Show_list")
    print ("6- Buy")
    print ("7- Create QR_Code")
    print ("8- Exit")

def add ():
    code = input ("Enter code:  ")
    name = input ("Enter name:  ")
    price = input ("Enter price:  ")
    count = input ("Enter count:  ")

    new_product = {'code' : code , 'name': name , 'price' : price , 'count' : count}

    PRODUCTS.append (new_product)

def edit ():
    user_input = input ( "enter code of product that you want to edit:  ")
    print ("1: edit name")
    print ("2: edit price")
    print ("3: edit count")
    choice = int (input ( "type your choice : " ) )

    for product in PRODUCTS :
        if product ['code'] == user_input :
            if choice == 1 :
                product ['name'] = input ("type new name...")
                
            elif choice == 2 :
                product ['price'] = input ("type new price...")

            elif choice == 3 :
                product ['count'] = input ("type new count...")

            else :
                print ("Invalid choice")

            print ("data has been edited successfully")
            break
    else :
        print ("no product with this code was found")

def remove ():
    user_input = input ( "enter code of product that you want to remove:  ")
    
    for product in PRODUCTS :
        if product ['code'] == user_input :
            PRODUCTS.remove (product)
            

            print ("this product has been removed successfully")
            break
    else :
        print ("no product with this code was found")
def search ():
    user_input = input ("type your keyword:  ")
    for product in PRODUCTS:
        if product['code'] == user_input or product['name'] == user_input :
            print (product['code'],"\t\t", product ['name'], "\t\t", product['price'])
            break
    else :
        print ("not found")

def show_list ():
    table = prettytable.PrettyTable ( )
    table.field_names = ["Code" , "Name" , "Price"]
    for product in PRODUCTS:
        table. add_row ([ product['code'], product ['name'],  product['price']])
    
    print ( table )

def buy ():
    shopping_list = []
    

    row = 0
    total_cost = 0

    while True:
        product_code = input ("type the desired product code to add to be added to shopping list :  ")
        
        for product in PRODUCTS :
            if product ['code'] == product_code :
                while True :
                    customer_count = input ( "How many/much this product do you want ? ")
                    if int (product ['count']) >= int (customer_count) :
                        row += 1
                        customer_list = {'row' : row , 'product' : product ['name'] , 'count' : customer_count , 'price/unit'  : product ['price'] , 'total price' : int (product ['price']) * int (customer_count)}
                        shopping_list . append (customer_list)
                        total_cost += int (customer_list ["total price"])
                        product ['count'] =  int (product ['count']) - int (customer_count)
                        break

                    else :
                        print ("Inventory of this product is insufficient ")
                        print ( "you can buy less than ", product ['count'])
                        change_count = input ( "if you want to change your count, press 1    ")
                        if change_count != "1" :
                            print ( "this product will not be added to the shopping list")
                            break

                
                break
        else :
            print ("no product with this code was found")
        add_product = input ( "if you want to add new product to shopping list, press 1    ")
        if add_product != "1" :
            if row > 0 :
                print ( "thank you for shopping")
            else :
                print ("No product has been purchased ")
            break
        
    
    if row > 0 :
        print ("Purchase invoice")
        table = prettytable . PrettyTable ()
        table. field_names = ["Row","Product name","Count","Price/unit","Total price"]

        #print ("Row\tProduct name\t\tCount\t\tPrice/unit\t\tTotal price")
        for item in shopping_list :
            table.add_row ( [ item['row'], item ['product'], item['count'], item['price/unit'], item['total price'] ] )

            #print (item['row'],"\t",item ['product'],"\t\t",item['count'],"\t\t",item['price/unit'],"\t\t",item['total price'])
        
        #print ("Total cost:\t\t\t",total_cost)
        table.add_row(["","","","",""],divider=True)
        table.add_row (["Total cost:","","","",total_cost])
        print (table)


def write_to_database():
    f = open ("database.txt","w")

    for product in PRODUCTS :
        line = product['code'] + "," + product['name'] + "," + product['price'] + "," + str( product['count'] ) + "\n"
        #print (line)
        f.write (line)

    f.close ()

def QRCOde ():
    user_input = input ( "enter code of product that you want to create a QR_Code:  ")
    for product in PRODUCTS :
        if product ['code'] == user_input :
            filename = product ['code'] + product ['name'] + ".png"
            image = qrcode.make (product)
            image.save(filename)
            print ("this product has been removed successfully")
            break
    else :
        print ("no product with this code was found")

print ("Welcome to my Store")
print ( "Loading...")
read_from_database ()
print ("Data loaded")

while True:
    show_menu()
    choice = int ( input ("Enter your choice: " ) )
    if choice == 1 :
        add ()
    elif choice == 2 :
        edit ()
    elif choice == 3 :
        remove ()   
    elif choice == 4 :
        search ()
    elif choice == 5 :
        show_list ()
    elif choice == 6 :
        buy ()
    elif choice == 7 :
        QRCOde() 
    elif choice == 8 :
        write_to_database ()
        exit (0)
    else:
        print ("Invalid input")