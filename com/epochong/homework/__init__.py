def isSu(n):
    if n == 2:
        return True
    for i in range(2,int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True
print("1-100的素数为")
for i in range(1,101):
    bool = isSu(i)
    if isSu(i):
        print(i,end = " ")