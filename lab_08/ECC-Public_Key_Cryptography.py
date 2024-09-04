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


def doc_subtraction(A, a, p, k):
    tmp = A
    flag = 1
    result = [0, 0]
    while k != 0:
        if k & 1 == 1:
            if flag == 1:
                result = tmp
                flag = 0
            else:
                result = add(result, tmp, a, p)
        k = k >> 1
        tmp = add(tmp, tmp, a, p)
    return result


def add(A, B, a, p):
    C = [0] * 2
    if A == B:
        m = pow(((3 * pow(A[0], 2) + a) * verse(2 * A[1], p)), 1, p)
    else:
        m = pow((int(B[1] - A[1]) * verse((B[0] - A[0]), p)), 1, p)
    C[0] = pow(int(pow(m, 2)) - A[0] - B[0], 1, p)
    C[1] = pow(int(m * (A[0] - C[0])) - A[1], 1, p)
    return C


def diminish(A, B, a, p):
    if A == B:
        return [0, 0]
    else:
        B[1] = -B[1]
        return add(A, B, a, p)


def encrypted(p, a, b, G, PM, k, PB):
    C = [0,0]
    C[0] = doc_subtraction(G, a, p, k)
    temp = doc_subtraction(PB, a, p, k)
    C[1] = add(temp, PM, a, p)
    return C


def decrypted(p, a, C1, C2, nb):
    temp = doc_subtraction(C1, a, p, nb)
    result = diminish(C2, temp, a, p)
    return result


def main():
    p = int(input())
    a = int(input())
    b = int(input())
    G = [int(x) for x in input().split()]
    op = int(input())
    if op == 1:
        # 明文点
        PM = [int(x) for x in input().split()]
        # 随机数
        k = int(input())
        # 公钥点
        PB = [int(x) for x in input().split()]
        result = encrypted(p, a, b, G, PM, k, PB)
        for num in result:
            for num2 in num:
                print(num2, end=' ')
            print("")
    else:
        C1 = [int(x) for x in input().split()]
        C2 = [int(x) for x in input().split()]
        nb = int(input())
        result = decrypted(p, a, C1, C2, nb)
        for num in result:
            print(num, end=' ')


if __name__ == "__main__":
        main()
