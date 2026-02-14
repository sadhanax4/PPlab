import random
sum=0;
num=[];
even_count=0
for i in range(20):
    a = random.randrange(1,100)
    num.append(a)
    print(a,end=" ");
    sum+=a;
    if a % 2 == 0:
        even_count += 1
    Average=sum/20
print("\nAverage is: ",sum)
largest=max(num)
smallest=min(num)
num_sorted = sorted(list(set(num)))
second_smallest = num_sorted[1]
second_largest = num_sorted[-2]
print("largest value:",largest)
print("smallest value: ",smallest)
print("Second largest:", second_largest)
print("Second smallest:", second_smallest)
print("Number of even values:", even_count)
