# 二进制多项式除法(得到余数）
def mod(a, b):
    while a.bit_length() >= b.bit_length():  # 当 a 的位数大于等于 b 的位数时
        a ^= b << (a.bit_length() - b.bit_length())  # 将 a 的最高位与 b 对齐，并进行异或操作
    return a


# 二进制多项式除法（得到除数）
def div(a, b):
    res = 0
    while a.bit_length() >= b.bit_length():
        res |= 1 << (a.bit_length() - b.bit_length())  # 将 res 的对应位设为 1
        a ^= b << (a.bit_length() - b.bit_length())  # 将 a 的最高位与 b 对齐，并进行异或操作
    return res


# 二进制多项式乘法
def mul(a, b):
    poly = 0x11b  # 不可约多项式
    res = 0
    while b:
        if b & 1:
            res ^= a  # 如果 b 的最低位为 1，则将结果与 a 异或
        a <<= 1  # a 左移一位
        if a & 0x100:
            a ^= poly  # 如果 a 的最高位为 1，则与不可约多项式进行异或操作
        b >>= 1  # b 右移一位
    return res


# 扩展欧几里得算法
def exEuclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x_temp, y_temp = exEuclid(b, mod(a, b))
        x, y = y_temp, x_temp ^ mul(y_temp, div(a, b))
        return gcd, x, y


# S 盒逆运算
def s_inv(s):
    res = []
    for i in range(256):
        _, temp, _ = exEuclid(s[i], 0x11b)  # 使用扩展欧几里得算法计算逆元
        res.append(temp)
    return res


# 字节变换
def ByteImage(s):
    res = [0 for _ in range(256)]
    temp = 0x63
    for i in range(256):
        a = s[i]
        for j in range(8):
            res[i] += (((a >> j) & 0x1) ^ ((a >> ((j + 4) % 8)) & 0x1) ^ ((a >> ((j + 5) % 8)) & 0x1) ^ (
                    (a >> ((j + 6) % 8)) & 0x1) ^ ((a >> ((j + 7) % 8)) & 0x1) ^ ((temp >> j) & 0x1)) << j
    return res


# 输出成 16 进制格式
def bit_16(s):
    for i in range(256):
        print("0x%02x" % s[i], end=' ')
        if i % 16 == 15:
            print()


# S 盒逆映射
def sinv(s):
    res = [0 for _ in range(256)]
    for i in range(len(s)):
        res[s[i]] = i
    return res

def main():
    s = [i for i in range(256)]
    bit_16(s)
    print("\n")

    s = s_inv(s)
    bit_16(s)
    print("\n")

    s = ByteImage(s)
    bit_16(s)
    print("\n")

    s = sinv(s)
    bit_16(s)


if __name__ == "__main__":
    main()
