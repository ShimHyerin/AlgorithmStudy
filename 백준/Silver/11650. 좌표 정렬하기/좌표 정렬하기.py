n = int(input())
num_list = []
for _ in range(n):
    a, b = map(int, input().split())
    t = a, b
    num_list.append(t)

num_list.sort()

for i in num_list:
    print(i[0], i[1])