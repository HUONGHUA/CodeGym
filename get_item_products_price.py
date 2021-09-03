products = {
            'SMART WATCH': 550,
            'PHONE' : 1000,
            'PLAYSTATION': 500,
            'LAPTOP' : 1550,
            'MUSIC PLAYER' : 600,
            'TABLET' : 400
           }

def display_products(product_db,price):
    for item in product_db:
        if product_db[item] <= price:
            print(item ,":",product_db[item])
input_price = int(input("Please enter price :"))
display_products(products,input_price)
