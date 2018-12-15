n = int(input())
a = int(input())

if a > n:
	while a%n != 0 :
		temp = a
		a = n
		n = temp%n
	print(n)
if n > a:
	while n%a != 0 :
		temp = n
		n = a
		a = temp%a
	print(a)