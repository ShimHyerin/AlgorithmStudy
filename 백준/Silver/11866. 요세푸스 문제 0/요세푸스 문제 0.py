n, k = map(int, input().split())
q = []
for i in range(1, n+1):
	q.append(i)
print('<', end='')
while len(q) != 1:
	for i in range(k-1):
		q.append(q[0])
		q.pop(0)
	print(q[0], end=', ')
	q.pop(0)
print(q[0], end='>')