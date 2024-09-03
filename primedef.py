def prime(num):
    count=0
    for i in range(2,(int)(num/2)+1):
        if num%i==0:
            count+=1
        return count
num=int(input("enter no: "))
count=prime(num)
if count==0:
    print("prime")
else:
    print("not")
