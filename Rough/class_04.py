def greeting():
    print("Hallo World")

greeting()

# Virtual Environments
# .venv\Scripts\activate
def items(*n):
    print(sum(n))

items(12,2,2,6)

def my_total(*x):
    sum = 0
    for i in x:
        sum += i
    print("x =", sum)

my_total(1,2,3,4,5,6,7,8,9,10)