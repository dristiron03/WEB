b = list(map(int,input().split()))
b.sort()
a = {}
for i in range(len(b)):
	if b[i] not in a :
		a[b[i]] = 1
	else:
		a[b[i]] += 1
for b[i] in a:
	print(b[i],":",a[b[i]])