def GF_operations(x, op, y):
    if op == '+':
        add = x ^ y
        return add
    elif op == '-':
        dim = x ^ y
        return dim
    elif op == '*':
        ans = 0
        while y > 0:
            if y & 1 == 1:
                ans ^= x
            x <<= 1
            if x & 0x100 == 0x100:
                x ^= 0x11b
            x &= 0xff
            y >>= 1
        return ans
    elif op == '/':
        if y == 1:
            return x, 0
        num1 = len(bin(x)[2:])
        num2 = len(bin(y)[2:])
        if num1 == num2:
            return 1, x ^ y
        elif num1 < num2:
            return 0, x
        else:
            ans = 0
            while num1 >= num2:
                rec = num1 - num2
                x ^= (y << rec)
                ans ^= (1 << rec)
                num1 = len(bin(x)[2:])
        return ans, x
    return -1


# 求逆元
def verse(e):
    f = 0x11b
    (x1, y1, x2, y2) = (1, 0, 0, 1)
    while f != 0:
        x1 = x1 ^ GF_operations(GF_operations(e, '/', f)[0], '*', x2)
        y1 = y1 ^ GF_operations(GF_operations(e, '/', f)[0], '*', y2)
        e = GF_operations(e, '/', f)[1]
        (c, x3, y3) = (e, x1, y1)
        (e, x1, y1) = (f, x2, y2)
        (f, x2, y2) = (c, x3, y3)
    return int(x1)


# 测试
x = input()
X = int(x, 16)
ANS = verse(X)
print('{:02x}'.format(ANS))
