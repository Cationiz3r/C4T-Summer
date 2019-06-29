
book = {
    "name": "The Deventure of The Normie",
    "pubyear": "20XX",
    "characters": ["Stephen", "Dan", "Zane"],
}

book["manufactor"]= "Xapploie"
book["country"]= "The Publica of Boardein"

for k, v in book.items():
    print(k, "-", v)
print()

# Update List
book["characters"]= ["Anne", "Bran", "Cessi"]

# Create item in list
book["characters"].append("Dantey")

# Delete first item in list
book["characters"].pop(0)

# Print second in list
print(book["characters"][1])
print()

# Print each character
for char in book["characters"]:
    print(char)
print()

# Print All
for key, value in book.items():
    if key != "characters":
        print(key, end="")
        print(":", value)
    else:
        print(key, end=": ")
        for index in range(len(value)):
            if index < len(value) -1:
                print(value[index], end=", ")
            else:
                print(value[index])