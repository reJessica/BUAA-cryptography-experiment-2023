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


# 快速模幂算法
def quickmod(m, e1, N2):
    list2 = [0] * len(bin(e1)[2:])
    temp = m
    re = 1
    for i in range(len(bin(e1)[2:])):
        list2[i] = temp
        temp = (temp * temp) % N2
    temp = e1
    for i in range(len(bin(e1)[2:])):
        if ((temp & 1) | 0) == 1:
            re = (re * list2[i]) % N2
        temp = temp >> 1
    return re


# 用中国剩余定理优化 RSA 的解密速度。
def CRT(c, p, q, e):
    d1 = (verse(e, p - 1) + p - 1) % (p - 1)
    d2 = (verse(e, q - 1) + q - 1) % (q - 1)
    red1 = (verse(q, p) + p) % p
    red2 = (verse(p, q) + q) % q
    return (q * red1 * quickmod(c, d1, p) + p * red2 * quickmod(c, d2, q) + p * q) % (p * q)


def RSA(P, Q, E, M, OP):
    N = P * Q
    # 加密模式
    if OP == 1:
        c = quickmod(M, E, N)
    # 解密模式
    else:
        c = CRT(M, P, Q, E)
    return c


def main():
    # 五行输入
    p = input().strip()
    q = input().strip()
    e = input().strip()
    m = input().strip()
    op = input().strip()
    result = RSA(int(p), int(q), int(e), int(m), int(op))
    print(result)


if __name__ == "__main__":
        main()
