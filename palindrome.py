n=int(input("enter the no: "))
t=n;
sum=0;
while(n>0):
    r=n%10
    sum=(sum*10)+r
    n=n//10
if(sum==t):
    print(t, " is palindrome");
else:
    print(t, " not");
