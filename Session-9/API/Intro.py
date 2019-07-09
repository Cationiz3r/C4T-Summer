import requests
import json

usersReq = requests.get("https://jsonplaceholder.typicode.com/users")
usersJson = usersReq.json()

print()
inputName = input("  Username: ")
print()

found = False
for user in usersJson:
    if (user["username"] == inputName):
        print("  Location:")
        print("    Lat:", user["address"]["geo"]["lat"])
        print("    Lng:", user["address"]["geo"]["lng"])
        print()

        found = True
        break

if (not found):
    print("  User not found!\n")
