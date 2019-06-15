# Count digit
# Actually session 6

print()
n = int(input("  Enter a number: "))
print()

if n == 0:
    digit = 1
else: 
    digit = 0
    while n > 0 or n < -1:
        n = n // 10
        digit += 1

print("  The number you entered has", digit, "digits")
print()
