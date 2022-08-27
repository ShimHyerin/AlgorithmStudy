import sys
input = sys.stdin.readline

# input
n = int(input())

shortcut = [] # 단축키
for _ in range(n):
    inp = input().split()
    flag = 0
    
    for i in range(len(inp)):
        if inp[i][0] not in shortcut:
            shortcut.append(inp[i][0].upper())
            shortcut.append(inp[i][0].lower())
            inp[i] = inp[i].replace(inp[i][0], f'[{inp[i][0]}]', 1)
            # print(*inp)

            flag = 1
            break
    
    if not flag:
        for i in range(len(inp)):
            for j in range(len(inp[i])):
                if inp[i][j] not in shortcut:
                    shortcut.append(inp[i][j].upper())
                    shortcut.append(inp[i][j].lower())
                    inp[i] = inp[i].replace(inp[i][j], f'[{inp[i][j]}]', 1)
                    # print(*inp)
                    flag = 1
                    break
            if flag: break
    print(*inp)
    