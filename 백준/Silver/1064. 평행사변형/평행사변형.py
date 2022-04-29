import math

dot = list(map(int, input().split()))
# 기울기
a = math.sqrt((dot[5] - dot[1]) ** 2 + (dot[4] - dot[0]) ** 2)
b = math.sqrt((dot[3] - dot[5]) ** 2 + (dot[2] - dot[4]) ** 2)
c = math.sqrt((dot[1] - dot[3]) ** 2 + (dot[0] - dot[2]) ** 2)
anw = (max(a, max(b, c)) * 2 - min(a, min(b, c)) * 2)
if ((dot[2] - dot[0]) * (dot[5] - dot[1])) == ((dot[3] - dot[1]) * (dot[4] - dot[0])):
    print(-1)
else: print(anw)
