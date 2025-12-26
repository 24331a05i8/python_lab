base=int(input("enter base:"))
exponent=int(input("enter exponent:"))
result=1
for i in range(exponent):
  result=result*base
print("result=",result)
