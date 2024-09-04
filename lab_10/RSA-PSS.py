import hashlib
import math

hLen = 20
sLen = 20


def Mod_fast(a, b, p):
    tmp = a % p
    result = 1
    while b != 0:
        if b & 1 == 1:
            result = (result * tmp) % p
        b = b >> 1
        tmp = (tmp * tmp) % p
    return result


def sha1_hash(data: bytes) -> bytes:
    sha1 = hashlib.sha1()
    sha1.update(data)
    return sha1.digest()


# 产生公钥/私钥过程

# 掩码产生函数
def MGF_1(X, maskLen):
    global hLen, sLen
    T = b''
    K = math.ceil(maskLen / hLen)
    for i in range(K):
        C = i.to_bytes(4, byteorder='big')
        T += sha1_hash(X + C)
    return T[:maskLen]


# 签名
def sign(M, n, emBits, d, salt):
    global hLen, sLen
    m_hash = sha1_hash(M)  # hash值只有20字节,type为str,16进制每2个字符表示一个字节
    M1 = b'\x00' * 8 + m_hash + salt
    H = sha1_hash(M1)  # 16进制字符串
    emLen = math.ceil(emBits / 8)
    DB = b'\x00' * (emLen - sLen - hLen - 2) + b'\x01' + salt
    dbMask = MGF_1(H, emLen - hLen - 1)
    maskedDB = bytes(x ^ y for x, y in zip(DB, dbMask))
    maskedDB = bytes([maskedDB[0] & (0xff >> (8 * emLen - emBits))]) + maskedDB[1:]
    EM = maskedDB + H + b'\xbc'
    s = Mod_fast(int.from_bytes(EM, 'big'), d, n)
    return hex(s)[2:]


def vrfy(M, n, emBits, e, S):
    global hLen, sLen
    m_hash = sha1_hash(M)
    m = Mod_fast(S, e, n)
    print(m)
    emLen = math.ceil(emBits / 8)
    EM = m.to_bytes(emLen, 'big')
    if emLen < hLen + sLen + 2:
        return False
    elif EM[-1] != 0xBC:
        return False
    else:
        maskedDB = EM[:(emLen - hLen - 1)]
        H = EM[(emLen - hLen - 1):(emLen - 1)]
        if maskedDB[0] & (0xff << (8 - 8 * emLen + emBits)):
            return False
        dbMask = MGF_1(H, emLen - hLen - 1)
        DB = bytes(x ^ y for x, y in zip(maskedDB, dbMask))
        DB = bytes([DB[0] & (0xff >> (8 * emLen - emBits))]) + DB[1:]
        if DB[:(emLen - hLen - sLen - 1)] != b'\x00' * (emLen - sLen - hLen - 2) + b'\x01':
            return False
        salt = bytes(DB[-sLen:])
        M1 = b'\x00' * 8 + m_hash + salt
        H2 = sha1_hash(M1)
        return H == H2


def main():
    M = input().strip().encode('utf-8')  # 字节类型
    n = int(input().strip())  # int类型
    emBits = int(input().strip())  # int类型
    Mode = input().strip()  # 字符串类型
    if Mode == 'Sign':
        d = int(input().strip())  # 私钥
        salt = bytes.fromhex(input().strip())  # 公钥,将输入的十六进制字符串转换成字节对象
        result = sign(M, n, emBits, d, salt)
        print(result)
    else:
        e = int(input())  # 签名所需
        S = int(input(), 16)  # 签名
        result = vrfy(M, n, emBits, e, S)
        print(result)


if __name__ == "__main__":
    main()
