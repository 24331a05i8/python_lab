#pass by value
def change(x):
    x = "siri"
a = "sri"
change(a)
print(a)
#pass by referance
def change(list1):
    list1[1] = 10

a = [5,10,35]
change(a)
print(a)
