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


# 计算一个方阵的伴随矩阵
def cofactor_matrix(matrix):
    n = len(matrix)
    adjugate = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            cofactor = (-1) ** (i + j) * determinant(minor)
            adjugate[j][i] = cofactor

    return adjugate


# 计算一个方阵的行列式
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(n):
            minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
            det += (-1) ** j * matrix[0][j] * determinant(minor)
        return det


# 矩阵相乘
def matrix_multiplication(mareix1, matrix2):
    # 初始化元素个数为0
    num_elements = 0

    # 遍历矩阵并计算元素个数
    for row in mareix1:
        num_elements += len(row)

    cols1 = len(mareix1[0])
    row1 = num_elements // cols1
    cols2 = len(matrix2[0])
    RE = [[None for _ in range(cols2)] for _ in range(row1)]
    # 第2~n+1行
    for i in range(row1):
        for j in range(cols2):
            tmp = 0
            for k in range(cols1):
                tmp += (mareix1[i][k] * matrix2[k][j])
            RE[i][j] = int(tmp)
    return RE


# Hill密码
def Hill_Code(KEY, S, OP):
    cols2 = len(KEY[0])
    rows2 = len(S) // cols2
    Message = [[None for _ in range(cols2)] for _ in range(rows2)]
    index_row = 0
    index_cols = 0
    result = ""
    for char in S:
        Message[index_row % rows2][index_cols] = ord(char) - 97
        if index_cols == cols2 - 1:
            index_cols = 0
            index_row += 1
        else:
            index_cols += 1
    if OP == 1:
        code = matrix_multiplication(Message, KEY)
        for row in code:
            for elem in row:
                if elem is not None:
                    result = result + chr(elem % 26 + 97)
        return result
    else:
        Cofactor_matrix = (cofactor_matrix(KEY))
        Cofactor_matrix2 = []
        for i in range(len(Cofactor_matrix)):
            row = []
            for j in range(len(Cofactor_matrix[i])):
                new_element = (verse(determinant(KEY), 26) * Cofactor_matrix[i][j]) % 26
                row.append(new_element)
            Cofactor_matrix2.append(row)
        code = matrix_multiplication(Message, Cofactor_matrix2)
        for row in code:
            for elem in row:
                if elem is not None:
                    result = result + chr(elem % 26 + 97)
        return result


def main():
    # 输入
    # 第1行
    n = int(input())
    rows = int(n)
    cols = rows
    Key = [[None for _ in range(cols)] for _ in range(rows)]
    # 第2~n+1行
    for i in range(int(n)):
        Key[i] = input().strip().split(" ")
    Key_int = [[int(elem) for elem in row] for row in Key]
    # 第n+2行
    s = input().strip()
    # 第n+3行
    op = input()
    result = Hill_Code(Key_int, s, int(op))
    print(result)


if __name__ == "__main__":
    main()
