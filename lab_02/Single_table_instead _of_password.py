def Single(T1, T2, S, OP):
    code = ""
    # 加密模式
    if OP == 1:
        for char in S:
            index = T1.find(char)
            code = code + T2[index]
        return code
    # 解密模式
    else:
        for char in S:
            index = T2.find(char)
            code = code + T1[index]
        return code


def main():
    # 输入
    t1 = input().strip()
    t2 = input().strip()
    s = input().strip()
    op = input()
    result = Single(t1, t2, s, int(op))
    print(result)


if __name__ == "__main__":
        main()
