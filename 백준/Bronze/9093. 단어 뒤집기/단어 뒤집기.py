n = int(input())


for _ in range(n):
	li = list(input().split())
	
	
	for i in li:
		print(i[::-1], end=' ')
	print()