
# init
storage = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30,
    "TOSHIBA": 10,
    "FUJITSU": 15,
    "ALIENWARE": 5,
}

price = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 12000,
    "ASUS": 400,
    "ACER": 350,
    "TOSHIBA": 600,
    "FUJITSU": 900,
    "ALIENWARE": 1000,
}

print()
product= input("  Enter products: ")
quantity= int(input("  Enter quantity: "))
product= product.upper()
print()
if product in storage:
    print("  Price:", price[product] *quantity, "\n")
else:
    print("  Products are not found!\n")