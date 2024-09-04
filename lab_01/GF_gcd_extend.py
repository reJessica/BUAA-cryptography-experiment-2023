def GF_operations(X, op, Y):
    if op == '*':
        ans = 0
        while Y > 0:
            if Y & 1 == 1:
                ans ^= X
            X <<= 1
            if X & 0x100 == 0x100:
                X ^= 0x11b
            X &= 0xff
            Y >>= 1
        return ans
    elif op == '/':
        if Y == 1:
            return X, 0
        num1 = len(bin(X)[2:])
        num2 = len(bin(Y)[2:])
        if num1 == num2:
            return 1, X ^ Y
        elif num1 < num2:
            return 0, X
        else:
            ans = 0
            while num1 >= num2:
                rec = num1 - num2
                X ^= (Y << rec)
                ans ^= (1 << rec)
                num1 = len(bin(X)[2:])
        return ans, X
    return -1


# 计算最大公因数
def GCD_normal(c, d):
    while d != 0:
        tmp = c
        c = d
        d = GF_operations(tmp, '/', d)[1]
    else:
        return c


# 扩展欧几里得算法数论算法
def GCD_extend(e, f):
    (x1, y1, x2, y2) = (1, 0, 0, 1)
    while f != 0:
        x1 = x1 ^ GF_operations(GF_operations(e, '/', f)[0], '*', x2)
        y1 = y1 ^ GF_operations(GF_operations(e, '/', f)[0], '*', y2)
        e = GF_operations(e, '/', f)[1]
        (c, x3, y3) = (e, x1, y1)
        (e, x1, y1) = (f, x2, y2)
        (f, x2, y2) = (c, x3, y3)
    return int(x1), int(y1), int(e)


# 测试
A, B = input().split(" ")
a = int(A, 16)
b = int(B, 16)
x, y, g = GCD_extend(a, b)
print('{:02x}'.format(x), '{:02x}'.format(y), '{:02x}'.format(g))
