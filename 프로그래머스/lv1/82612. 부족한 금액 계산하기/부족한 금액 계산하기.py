def solution(price, money, count):
    tmp = 0
    for i in range(1,count+1):
        tmp += price*i
    if tmp > money: return tmp - money
    else: return 0