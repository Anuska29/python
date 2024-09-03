
def pali(s):
    if (s==s[::-1]):
        return ("pali")
    else:
        print("not")
s=input("enter: ")
print( pali(s))
