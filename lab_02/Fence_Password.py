def Fence_Password(K, S, OP):
    rows = K
    cols = len(S) // K + 1
    matrix = [[None for _ in range(cols)] for _ in range(rows)]
    # 加密模式
    if OP == 1:
        index_row = 0
        index_cols = 0
        code = ""
        for char in S:
            matrix[index_row % K][index_cols] = char
            index_row += 1
            if index_row % K == K - 1:
                index_cols += 1
        for row in matrix:
            for elem in row:
                if elem is not None:
                    code = code + elem
        return code
    # 解密模式
    else:
        index_row = 0
        index_cols = 0
        code = ""
        left = len(S) % K
        for char in S:
            matrix[index_row % K][index_cols] = char
            index_cols += 1
            if index_cols == len(S) // K:
                if left != 0:
                    left -= 1
                    continue
                else:
                    index_row += 1
                    index_cols = 0
                continue
            if index_cols > len(S) // K:
                index_row += 1
                index_cols = 0
                continue

        for index_cols2 in range(cols):
            for index_row2 in range(rows):
                elem = matrix[index_row2][index_cols2]
                if elem is not None:
                    code = code + elem
        return code


def main():
    # 输入
    k = input()
    s = input().strip()
    op = input()
    print(Fence_Password(int(k), s, int(op)))


if __name__ == "__main__":
    main()
