
# init
storage = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30,
}

storage["TOSHIBA"]= 10
storage["FUJITSU"]= 15
storage["ALIENWARE"]= 5

storage["DELL"]+= 10
storage["MACBOOK"]-= 2

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
for key in storage:
    total= storage[key] *price[key]
    print(" ", key, end=": ")
    print(total)
print()