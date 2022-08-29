import sys
input = sys.stdin.readline

def sol(age, wei):
    if age > 17 or wei >= 80:
        return 'Senior'
    else: return 'Junior'

while True:
    inp = input().rstrip()
    if inp == '# 0 0': break
    else:
        inp = inp.split()
        print(inp[0], sol(int(inp[1]), int(inp[2])))