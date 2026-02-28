import random
sum=0;
num=[]
even_count=0
for i in range(20):
    a=random.randrange(1,100)
    num.append(a)
    print(a,end="");
    sum+=a;
    if a%2==0:
        even_count+=1
        average=sum/20
    print("\naverage is: ",sum)
    largest=max(num)
    smallest=min(num)
    num_sorted=sorted(list(set(num)))
    second_gratest=num_sorted[-2]
    print("largest value is: ",largest);
    print("smallest value is: ",smallest);
    print("second largest: ",second_largest);
    print("second smallest: ",second_smallest);
    print("number of even values: ",even_count);
