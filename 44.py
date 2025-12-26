a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
maximum=a
minimum=a
if(b>maximum):
    maximum=b
if(c>maximum):
    maximum=c
if(b<maximum):
    minimum=b
if(c<maximum):
    minimum=c
print("maximum:",maximum)
print("minimum:",minimum)
