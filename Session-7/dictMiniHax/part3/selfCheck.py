
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

for k, v in storage.items():
    print(" ", k, end=": ")
    print(v)