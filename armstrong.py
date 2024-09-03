n=int(input("enter no: "))
re=0
t=n
while(n>0):
    r=n%10
    re=(r*r*r)+re
    n=n//10
if re==t:
    print("armstrong")
else:
    print("not")
