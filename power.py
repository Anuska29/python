print("power of no")
base=int(input("base:"))
exponent=int(input("exponent:"))
result=1
for exponent in range(exponent,0,-1):
    result*=base
print("ans="+str(result))
