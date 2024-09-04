# 求最大公因数
def GCD_normal(a, b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % b
    else:
        return abs(a)


# 求逆元
def verse(a, b):
    (x1, y1, x2, y2) = (1, 0, 0, 1)
    while b != 0:
        x1 = x1 - (a // b) * x2
        y1 = y1 - (a // b) * y2
        a = a % b
        (c, x3, y3) = (a, x1, y1)
        (a, x1, y1) = (b, x2, y2)
        (b, x2, y2) = (c, x3, y3)
    return int(x1)


# 中国剩余定理
def CRT(a1, a2, a3, b1, b2, b3):
    M = a1 * a2 * a3
    (M1, M2, M3) = (a2 * a3, a1 * a3, a1 * a2)
    m1 = verse(M1, a1)
    m2 = verse(M2, a2)
    m3 = verse(M3, a3)
    re = (M1 * m1 * b1 + M2 * m2 * b2 + M3 * m3 * b3) % M
    if re < 0:
        while re < 0:
            re = re + abs(M)
        return re
    else:
        while re > 0:
            re = re - abs(M)
        return re + abs(M)


# 测试
A1, A2, A3 = map(int, input().split())
B1, B2, B3 = map(int, input().split())
result = CRT(A1, A2, A3, B1, B2, B3)
print(result)
