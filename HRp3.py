# Enter your code here. Read input from STDIN. Print output to STDOUT
a = list(map(str,input()))
i = 0
b = 0
while i < len(a):
    k = 0
    for j in range (i,len(a)):
        if a[i] == a[j] :
            k = k + 1
        else:
            b = 0
            break 
    if b == 0:
        g = '('
        f = ", "
        h = ")"
        print(g+str(k)+f+str(a[i])+h,end=" ")
        i = i+int(k)
    
