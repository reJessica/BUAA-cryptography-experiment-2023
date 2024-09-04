
def Virginia_Code(K, S, OP):
    code = ""
    d = len(K)
    # 加密模式
    if OP == 1:
        index = 0
        for char in S:
            char_ord = ord(char) - 97
            K_ord = ord(K[index % d]) - 97
            code = code + chr((char_ord + K_ord) % 26 + 97)
            index += 1
        return code
    # 解密模式
    else:
        index = 0
        for char in S:
            char_ord = ord(char) - 97
            K_ord = ord(K[index % d]) - 97
            code = code + chr((char_ord - K_ord) % 26 + 97)
            index += 1
        return code


def main():
    # 输入
    k = input().strip()
    s = input().strip()
    op = input()
    result = Virginia_Code(k, s, int(op))
    print(result)


if __name__ == "__main__":
        main()
