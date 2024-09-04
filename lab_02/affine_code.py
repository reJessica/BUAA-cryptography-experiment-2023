def GCD_normal(a, b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % b
    else:
        return a


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


def affine_coded(k, b, s, op):
    code = ""
    if GCD_normal(26, k) != 1:
        code = "invalid key"
        return code
    # 解密情况
    if op == 0:
        for char in s:
            char_ord = ord(char) - 97
            code = code + chr((26 + (char_ord - b) * verse(k, 26)) % 26 + 97)
        return code

    # 加密情况
    elif op == 1:
        for char in s:
            char_ord = ord(char) - 97
            code = code + chr((k * char_ord + b) % 26 + 97)
        return code


def main():
    # 输入
    K, B = 3, 17
    S = input()
    OP = int(input())
    out = affine_coded(int(K), int(B), S, int(OP))
    print(out)


if __name__ == "__main__":
    main()
