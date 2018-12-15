n = int(input())
for i in range(n):
	b = input()
	k=len(b)
	while k > 3:
		b = b[:k-3]+','+b[k-3:]
		k=k-3
	print(b)