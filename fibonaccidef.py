n=int(input("enter range: "))
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(3,1+n):
            c=a+b
            print(c)
            a=b
            b=c
print(fib(n))
