n = int(input())
for i in range(n):
    ip = input().split()
    tmp = float(ip[0])
    ip = ip[1:]
    for j in ip:
        if j == '@':
            tmp *= 3
        elif j == '%':
            tmp += 5
        else:
            tmp -= 7
    print(f'{tmp:.2f}')  