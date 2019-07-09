
def modify2(a):
    a = 9

def modify(x):
    x = 5
    modify2(x)

stuff = 8
modify(stuff)
print(stuff)