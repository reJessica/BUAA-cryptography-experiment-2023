import hashlib
import random


def Mod_fast(a, b, p):
    tmp = a % p
    result = 1
    while b != 0:
        if b & 1 == 1:
            result = (result * tmp) % p
        b = b >> 1
        tmp = (tmp * tmp) % p
    return result


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


def ElGamal_sign(q, a, M, XA, K):
    m = int(hashlib.sha256(M.encode()).hexdigest(), 16)
    S1 = Mod_fast(a, K, q)
    k_ver = verse(K, q - 1)
    # print(k_ver)
    S2 = Mod_fast(k_ver * (m - XA * S1), 1, q - 1)
    return S1, S2


def ElGamal_vrfy(q, a, M, YA, S1, S2):
    # print(S1, S2)
    m = int(hashlib.sha256(M.encode()).hexdigest(), 16)
    v1 = Mod_fast(a, m, q)
    v2 = Mod_fast(Mod_fast(YA, S1, q) * Mod_fast(S1, S2, q), 1, q)
    # print(v2)
    return v1 == v2


def main():
    q = int(input())  # 参数中的素数
    a = int(input())  # 参数中的原根
    M = input()  # 签名消息
    Mode = input()  # 代表签名or验证
    if Mode == 'Sign':
        XA = int(input())  # 签名方的私钥
        K = int(input())  # 签名所需要的随机数
        (S1, S2) = ElGamal_sign(q, a, M, XA, K)
        print(str(S1) + " " + str(S2))
    else:
        YA = int(input())
        S = input()
        S1, S2 = S.split()
        S1 = int(S1)
        S2 = int(S2)
        FLAG = ElGamal_vrfy(q, a, M, YA, S1, S2)
        print(FLAG)


