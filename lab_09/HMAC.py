# 初始化
import os
import random
import string
from hashlib import sha1

H0 = [0] * 512
H1 = [0] * 512
H2 = [0] * 512
H3 = [0] * 512
H4 = [0] * 512
H0[0] = int('67452301', 16)
H1[0] = int('efcdab89', 16)
H2[0] = int('98badcfe', 16)
H3[0] = int('10325476', 16)
H4[0] = int('c3d2e1f0', 16)


# 分组进行运算
def grouping_operation(binary_M):
    global H0, H1, H2, H3, H4
    group_num = len(binary_M) // 512
    group_M = [0] * group_num
    flag = 0
    # print(group_num)
    for i in range(group_num):
        # print(i)
        group_M[i] = binary_M[i * 512:(i + 1) * 512]
    # print(group_M)
    for j in range(group_num):
        a = H0[j]
        b = H1[j]
        c = H2[j]
        d = H3[j]
        e = H4[j]
        # print(hex(a), hex(b), hex(c), hex(d), hex(e))
        a, b, c, d, e = step_operation(a, b, c, d, e, group_M[j])
        H0[j + 1] = (H0[j] + a) % pow(2, 32)
        H1[j + 1] = (H1[j] + b) % pow(2, 32)
        H2[j + 1] = (H2[j] + c) % pow(2, 32)
        H3[j + 1] = (H3[j] + d) % pow(2, 32)
        H4[j + 1] = (H4[j] + e) % pow(2, 32)
        flag = j + 1
    return flag


# f函数
def f(x, y, z, t):
    if 0 <= t <= 19:
        return (x & y) | ((~x) & z)
    elif 20 <= t <= 39:
        return x ^ y ^ z
    elif 40 <= t <= 59:
        return (x & y) | (x & z) | (y & z)
    elif 60 <= t <= 79:
        return x ^ y ^ z
    else:
        return -1


# K函数
def K(t):
    if 0 <= t <= 19:
        return int('5a827999', 16)
    elif 20 <= t <= 39:
        return int('6ed9eba1', 16)
    elif 40 <= t <= 59:
        return int('8f1bbcdc', 16)
    elif 60 <= t <= 79:
        return int('ca62c1d6', 16)


# 步函数
def step_operation(a, b, c, d, e, group_M):
    W = [0] * 80
    # 扩充位
    for i in range(80):
        if i <= 15:
            W[i] = int(group_M[32 * i: 32 * i + 32], 2) % pow(2, 32)
        else:
            W[i] = ((W[i - 3] ^ W[i - 8] ^ W[i - 14] ^ W[i - 16]) << 1 | (
                    W[i - 3] ^ W[i - 8] ^ W[i - 14] ^ W[i - 16]) >> 31) % pow(2, 32)
        # print(i, hex(W[i]))
    for t in range(80):
        # print(t, hex(a), hex(b), hex(c), hex(d), hex(e))
        T = ((a << 5 | a >> 27) + f(b, c, d, t) + e + K(t) + W[t]) % pow(2, 32)
        e = d % pow(2, 32)
        d = c % pow(2, 32)
        c = (b << 30 | b >> 2) % pow(2, 32)
        b = a % pow(2, 32)
        a = T

    return a, b, c, d, e


# 主函数
def sha_1(M):
    # 补位操作
    utf8_encoded = M.encode('utf-8')
    binary_M = ''.join(format(byte, '08b') for byte in utf8_encoded)
    length = len(binary_M)
    binary_length = format(length, '064b')
    # print(len(binary_length))
    num_0 = (448 - (length % 512)) % 512 - 1
    binary_M += '1' + '0' * num_0 + binary_length
    # print(binary_M)
    # print(len(binary_M))
    pos = grouping_operation(binary_M)
    # print(hex(H0[0]))
    # print(hex(H0[1]), hex(H2[1]), hex(H3[1]), hex(H4[1]))
    result = '{:08x}'.format(int(H0[pos])) + '{:08x}'.format(int(H1[pos])) + '{:08x}'.format(
        int(H2[pos])) + '{:08x}'.format(int(H3[pos])) + '{:08x}'.format(int(H4[pos]))
    return result


# 定义生成随机字符串的函数
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def main():
    ipad = ''
    opad = ''
    for j in range(8):
        ipad += '00110110'
        opad += '01011010'
    k = input() #字符串
    M = input()
    len_k = len(k)
    if len_k > 512:
        k_new = int(sha_1(k), 16)
    else:
        k_new = int(bin(int(k, 16))[2:] + '0' * (512 - len_k), 2)

    k_1 = str(k_new ^ int(ipad, 2))
    k_2 = k_new ^ int(ipad, 2)
    binary_list = [k_1[i:i + 8] for i in range(0, len(k_1), 8)]  # 将二进制字符串按每8位分割成列表
    decimal_list = [int(binary, 2) for binary in binary_list]  # 将二进制转换为十进制
    char_list = [chr(decimal) for decimal in decimal_list]  # 将十进制转换为对应的字符
    encoded_string = ''.join(char_list)  # 将字符列表连接成字符串

    # 计算HMAC-SHA1值
    inner_hash = sha_1(encoded_string + M)
    tmp = bytes.fromhex(inner_hash)
    outer_hash = sha1(k_opad + tmp)

    # 返回HMAC-SHA1值的十六进制表示
    return outer_hash


if __name__ == '__main__':
    main()
