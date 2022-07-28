import sys
input = sys.stdin.readline

l = int(input())
s = input()
tmp = 'abcdefghijklmnopqrstuvwxyz'
alphabet = {}
for i in range(len(tmp)):
    alphabet[tmp[i]] = i+1

# r과 M은 서로소이다. 
r = 31 # 알파벳의 개수인 26보다 큰 소수
M = 1234567891

hash = 0
for i in range(l):
    hash += alphabet[s[i]] * (r**i)
# print(hash) # 50점 코드
print(hash%M) # mod 연산을 해주어야한다.