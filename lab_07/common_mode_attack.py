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
                    return int(x1 + i * Bx // a), int(y1 - i * Ax // a), int(a)
            else:
                x1 = x1 - i * Bx // a
                y1 = y1 + i * Ax // a
                if x1 < 0:
                    return int(x1 + i * Bx // a), int(y1 - i * Ax // a), int(a)


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


def Mod_fast(a, b, p):
    result = 1
    if b > 0:
        tmp = a % p
    else:
        tmp = verse(a % p, p)
        b = -b
    while b != 0:
        if b & 1 == 1:
            result = (result * tmp) % p
        b = b >> 1
        tmp = (tmp * tmp) % p
    return result



def common_mode_attack(e1, e2, c1, c2, N):
    s1, s2, gcd = GCD_extend(e1, e2)
    temp = Mod_fast(c1, s1, N) * Mod_fast(c2, s2, N)
    m = Mod_fast(temp, 1, N)
    return m


def main():
    e1 = int(input())
    e2 = int(input())
    c1 = int(input())
    c2 = int(input())
    N = int(input())
    result = common_mode_attack(e1, e2, c1, c2, N)
    print(result)


if __name__ == "__main__":
    main()

