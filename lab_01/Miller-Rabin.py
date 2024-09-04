# Miller-Rabin素性检测算法
import random


def Mod_fast(a, b, p):
    tmp = a % p
    result = 1
    while b != 0:
        if b & 1 == 1:
            result = (result * tmp) % p
        b = b >> 1
        tmp = (tmp * tmp) % p
    return result


def Miller_Rabin(n):
    q = n - 1
    k = 0
    while q % 2 != 1:
        q = q // 2
        k = k + 1
    for i in range(10):
        a = random.randint(1, n - 1)
        if Mod_fast(a, q, n) == 1:
            return 1
        for j in range(0, k):
            if Mod_fast(a, pow(2, j) * q, n) == n - 1:
                return 1
        return -1


# 测试
N = input()
if Miller_Rabin(int(N)) == 1:
    print("YES")
else:
    print("NO")
