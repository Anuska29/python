num=int(input("enter: "))
def armstrong(num):
    sum=0
    n1=len(str(num))
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**n1
        temp//=10
    if num==sum:
        print(num,"armstrong")
    else:
        print(num,"not")
armstrong(num)
