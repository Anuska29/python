n=int(input("enter range: "))
sum=0
s=0
for i in range(1,n+1,1):
    if(i%2==0):
        print("even" , i)
        sum=sum+i
    else:
        print("odd", i)
        s=s+i
print(" sum of odds: ", s)
print("sum of evens: ",sum)
