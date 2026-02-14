a=input("enter a string1: ")
b=input("enter a string2: ")
c=""
if(len(a)==len(b)):
    print("same length: ")
    for i in range(len(b)):
        c = c + a[i] + b[i]
    else:
        print("both are not same")
    print(c)
