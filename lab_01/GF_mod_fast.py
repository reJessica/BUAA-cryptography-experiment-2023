def GF_mul(x, y):
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


def GF_Mod_fast(a, b):
    tmp = a
    result = 1
    while b != 0:
        if b & 1 == 1:
            result = GF_mul(result, tmp)
        b = b >> 1
        tmp = GF_mul(tmp, tmp)
    return result


# 测试
x, y = input().split()
A = int(x, 16)
B = int(y)
ANS = GF_Mod_fast(A, B)
print('{:02x}'.format(ANS))
