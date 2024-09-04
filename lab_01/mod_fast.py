# 快速模幂算法
def Mod_fast(a, b, p):
    tmp = a % p
    result = 1
    while b != 0:
        if b & 1 == 1:
            result = (result * tmp) % p
        b = b >> 1
        tmp = (tmp * tmp) % p
    return result


# 测试
a, b, p = input().split(" ")
re = Mod_fast(int(a), int(b), int(p))
print(re)
