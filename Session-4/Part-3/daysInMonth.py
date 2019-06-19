
day = [31, "28 or 29 (Leap)", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print()
month = int(input("  Input month: "))
print()

if month > 12 or month < 1:
    print("  Bruh u serious?")
else:
    print("  Number of day in that month:", day[month - 1])

input()
    