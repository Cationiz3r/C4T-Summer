
# init
storage = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30,
}

print()
product= input("  Enter products: ")
product= product.upper()
print()
if product in storage:
    print("  Currently in storage:", storage[product], "\n")
else:
    print("  Products are not found!\n")