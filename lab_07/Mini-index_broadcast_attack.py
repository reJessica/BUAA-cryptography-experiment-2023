import gmpy2


# 求逆元
def verse(a, b):
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
                    return int(x1)
            else:
                x1 = x1 - i * Bx // a
                y1 = y1 + i * Ax // a
                if x1 > 0:
                    return int(x1)
    else:
        for i in range(10):
            if Bx > 0:
                x1 = x1 - i * Bx // a
                y1 = y1 + i * Ax // a
                if x1 < 0:
                    return int(x1 + i * Bx // a)
            else:
                x1 = x1 - i * Bx // a
                y1 = y1 + i * Ax // a
                if x1 < 0:
                    return int(x1 + i * Bx // a)


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
def CRT(ci, ni, n):
    N = 1
    result = 0
    M = [0] * 20
    Mv = [0] * 20
    for j in range(n):
        N = N * ni[j]
    for k in range(n):
        M[k] = N // ni[k]
        Mv[k] = verse(int(M[k]), ni[k])
        result = result + M[k] * Mv[k] * ci[k]
    return quickmod(result, 1, N)


def Mini_index_broadcast_attack(CI, NI, E, N):
    temp = int(CRT(CI, NI, N))
    m, demo = gmpy2.iroot(temp, E)
    return m


def main():
    ci = [0] * 20
    ni = [0] * 20
    N = input().strip()
    e = input().strip()
    for j in range(int(N)):
        ci[j] = int(input().strip())
        ni[j] = int(input().strip())
    result = Mini_index_broadcast_attack(ci, ni, int(e), int(N))
    print(result)


if __name__ == "__main__":
    main()
