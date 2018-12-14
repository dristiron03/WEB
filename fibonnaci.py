n = int(input())

sum=0
temp1=1
temp2=0
for i in range(n):
    print(sum)
    temp2 = temp1
    temp1 = sum
    sum = temp2 + temp1