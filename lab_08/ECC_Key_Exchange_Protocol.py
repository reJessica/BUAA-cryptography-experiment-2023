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


def add(A, B, a, p):
    if A[0] == B[0] and A[1] == -B[1]:
        return [0, 0]
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


def ECC_Key_Exchange_Protocol(p, a, b, G, XA, YB):
    result = doc_subtraction(YB, a, p, XA)
    return result


def main():
    p = int(input())
    a = int(input())
    b = int(input())
    G = [int(x) for x in input().split()]
    XA = int(input())
    YB = [int(x) for x in input().split()]
    result = ECC_Key_Exchange_Protocol(p, a, b, G, XA, YB)
    for num in result:
        print(num, end=' ')


if __name__ == "__main__":
    main()
