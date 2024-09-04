def Vernum_Code(K, S, OP):
    code = ""
    d = len(K)
    # 加解密模式
    if OP == 1:
        index = 0
        for char in S:
            char_ord = ord(char)
            K_ord = ord(K[index % d])
            code = code + chr(char_ord ^ K_ord)
            index += 1
        return code
    else:
        index = 0
        for char in S:
            char_ord = ord(char)
            K_ord = ord(K[index % d])
            code = code + chr(char_ord ^ K_ord)
            index += 1
        return code


def main():
    # 输入
    k = input().strip()
    s = input().strip()
    op = input()
    result = Vernum_Code(k, s, op)
    print(result)


if __name__ == "__main__":
        main()
