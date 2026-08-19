store = {}
cart = []
def load_products():
    with open("/home/hannanashraf/Documents/VS CODE/file handling practice/products.txt","r+") as file:
        for line in file:
            products,price,stock = line.strip().split(",")
            
            store[products] = {
                "price":int(price),
                "stock":int(stock)
            }
    return store
def save_products(store):
    with open("/home/hannanashraf/Documents/VS CODE/file handling practice/products.txt", "w") as file:
        for product, details in store.items():
            file.write(
                product + "," +
                str(details["price"]) + "," +
                str(details["stock"]) + "\n"
            )
def show_products():
    print("Available Items :")
    for products,details in store.items():
        print(products," | ","Price :",details["price"]," | ","Stock :",details["stock"])
def search_products(store):
    search = input("Enter Item Name To Search :").title()
    if search in store:
        item = store.get(search)
        print("Item Found.!")
        print(search," | ","Price :",item["price"]," | ","Stock :",item["stock"])
    else:
        print("Item Not Found In Inventory...!")
def buy_product(store,cart):
    product = input("Enter Item Name To Buy :")
    if product in store:
        stock = int(input("Enter Quantity You Required :"))
        if stock<= store[product]["stock"]:
            cart.append({
                "Product":product,
                "Price":store[product]["price"],
                "Quantity":stock
            })
            store[product]["stock"]-=stock
            print("Product Added To Cart Succesfully..!")
            save_products(store)
        else:
            print("Insufficient Stock.!\nWe Are Sorry For Inconvenience.")
    else:
        print("Product Not Found.!")
def add_product(store):
        product = input("Enter Product Name To Add in Store :")
        if product in store:
            print("Product Is Already In Inventory :")
        else:
            price = int(input("Enter Price Of Product :"))
            stock = int(input("Enter Stock In Inventory :"))
            store.update({
                product:{
                "price":price,
                "stock":stock
            }
            })
            print("Product Added Successfully.!")
            save_products(store)
def update_stock(store):
    product = input("Enter Item Name Of Which You Want To Update Stock :").title()
    found = False
    if product in store:
        stock = int(input("Enter Amount Of Stock :"))
        store[product]["stock"] = stock
        found = True
        print("Stock Updated.!")
        save_products(store)
    if not found:
        print("Product Not Found.!")
def delete_product(store):
    product = input("Enter Product Name To delete :")
    if product in store:
        store.pop(product)
        print("Product Deleted successfully.!")
        save_products(store)
    else:
        print("Product Not Found..!")
def show_cart(cart):
    print("Cart :",cart)
def show_bill(cart):
    total = 0 
    for item in cart:
        total += item["Price"] * item["Quantity"]
    print("--------------------")
    print("Total Bill = ",total)
def save_and_exit(store):
    save_products(store)
    print("Data Saved Successfully..!")
    print("Exiting...!/nThanks For Coming")
def main_menu():
    while True:
        print("1. Show Products\n2. Search Product\n3. Buy Product\n4. Add Product\n5. Update Stock\n6. Delete Product\n7. Show Cart\n8. Show Bill\n9. Save & Exit")
        choice = input("Enter Your Choice :")
        if choice == "1":
            show_products()
        elif choice == "2":
            search_products(store)
        elif choice == "3":
            buy_product(store,cart)
        elif choice == "4":
            add_product(store)
        elif choice == "5":
            update_stock(store)
        elif choice == "6":
            delete_product(store)
        elif choice == "7":
            show_cart(cart)
        elif choice == "8":
            show_bill(cart)
        elif choice == "9":
            save_and_exit(store)
            break
        else:
            print("Invalid Choice Entered.\nTry Again Plz ")
load_products()
main_menu()
            

        
        