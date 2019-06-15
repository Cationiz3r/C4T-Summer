# else if 0

print()
m = int(input("  Input Month = "))
print()

if m > 12 or m < 0:
    print("  Bruh u serious?")
elif m <= 3:
    print("  The currnet month is: Spring")
elif m <= 6:
    print("  The currnet month is: Summer")
elif m <= 9:
    print("  The currnet month is: Fall")
else:
    print("  The currnet month is: Winter")

print()