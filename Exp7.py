a=float(input("Enter a number"));
b=float(input("Enter a number"));
c=abs(a-b);
print(c)
if c<.001:
    print("Close")
else:
    print("Not Close")
