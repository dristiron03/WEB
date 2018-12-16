# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = {}
for i in range (n):
    b = input().split()
    x = b[0]
    for j in range (1,len(b)-1):
        x = x +" "+ b[j]
    if x not in a :
        a[x] = int(b[len(b)-1])
    else :
        a[x] += int(b[len(b)-1])

for k in a :
    print(k+" "+str(a[k]),end="\n")