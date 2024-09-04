# 矩阵密码
def matrix_code(N, K, S, OP):
    # 加密模式
    if OP == 1:
        # 矩阵处理
        cols = N
        rows = len(S) // N
        matrix = [[None for _ in range(cols)] for _ in range(rows)]
        index_row = 0
        index_cols = 0
        code = ""
        for char in S:
            matrix[index_row][index_cols] = char
            index_cols += 1
            if index_cols == cols:
                index_row += 1
                index_cols = 0
        for i in range(N):
            for j in range(rows):
                code = code + matrix[j][K.index(str(i + 1))]
        return code
    else:
        # 矩阵处理
        cols = N
        rows = len(S) // N
        matrix = [[None for _ in range(cols)] for _ in range(rows)]
        r = 0
        code = ""
        for i in range(N):
            for j in range(rows):
                matrix[j][K.index(str(i + 1))] = S[r]
                r += 1
        for rows in matrix:
            for elem in rows:
                code = code + elem
        return code


def main():
    # 输入
    n = input()
    k = input().strip()
    s = input().strip()
    op = int(input())
    result = matrix_code(int(n), k, s, int(op))
    print(result)


if __name__ == "__main__":
    main()
