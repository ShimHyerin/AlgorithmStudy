a, b = map(int,input().split())

def gcd(a,b):
    if b==0:
        return a
    else: return gcd(b,a%b)
gcd = gcd(a,b)
lcm = (a//gcd)*(b//gcd)*gcd
print(gcd)
print(lcm)