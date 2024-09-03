n=int(input("enter range: "))
f0=0;
f1=1;
print("fibonacci series is: ");
print(f0);
print(f1);
for i in range(2,n,1):
    f=f0+f1;
    f0=f1;
    f1=f;
    print(f)
