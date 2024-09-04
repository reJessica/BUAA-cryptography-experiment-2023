# 计算最大公因数
def GCD_normal(a, b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % b
    else:
        return a


# 扩展欧几里得算法数论算法
def GCD_extend(a, b):
    (Ax, Bx) = (a, b)
    (x1, y1, x2, y2) = (1, 0, 0, 1)
    while b != 0:
        x1 = x1 - (a // b) * x2
        y1 = y1 - (a // b) * y2
        a = a % b
        (c, x3, y3) = (a, x1, y1)
        (a, x1, y1) = (b, x2, y2)
        (b, x2, y2) = (c, x3, y3)
    # 接下来保证x是最小的正整数
    if a < 0:
        (x1, y1, a) = (-x1, -y1, -a)
    if x1 < 0:
        for i in range(10):
            if Bx > 0:
                x1 = x1 + i * Bx // a
                y1 = y1 - i * Ax // a
                if x1 > 0:
                    return int(x1), int(y1), int(a)
            else:
                x1 = x1 - i * Bx // a
                y1 = y1 + i * Ax // a
                if x1 > 0:
                    return int(x1), int(y1), int(a)
    else:
        for i in range(10):
            if Bx > 0:
                x1 = x1 - i * Bx // a
                y1 = y1 + i * Ax // a
                if x1 < 0:
                    return int(x1+i * Bx // a), int(y1-i * Ax // a), int(a)
            else:
                x1 = x1 - i * Bx // a
                y1 = y1 + i * Ax // a
                if x1 < 0:
                    return int(x1+i * Bx // a), int(y1-i * Ax // a), int(a)


# 测试
A, B = input().split(" ")
(x, y, gcd) = GCD_extend(int(A), int(B))
print(x, y, gcd)
