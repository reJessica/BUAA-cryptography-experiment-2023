def GF_operations(X, op, Y):
    if op == '*':
        ans = 0
        while Y > 0:
            if Y & 1 == 1:
                ans ^= X
            X <<= 1
            if X & 0x100 == 0x100:
                X ^= 0x11b
            X &= 0xff
            Y >>= 1
        return ans
    elif op == '/':
        if Y == 1:
            return X, 0
        num1 = len(bin(X)[2:])
        num2 = len(bin(Y)[2:])
        if num1 == num2:
            return 1, X ^ Y
        elif num1 < num2:
            return 0, X
        else:
            ans = 0
            while num1 >= num2:
                rec = num1 - num2
                X ^= (Y << rec)
                ans ^= (1 << rec)
                num1 = len(bin(X)[2:])
        return ans, X
    return -1


# 计算最大公因数
def GCD_normal(c, d):
    while d != 0:

        tmp = c
        c = d
        d = GF_operations(tmp, '/', d)[1]
    else:
        return c


# 判断多项式是否不可约
def identity(A):
    max = pow(2, 9)
    for k in range(2, max):
        if GCD_normal(k, A) > 1 and k != A:
            return False
    return True


# 本原多项式的判定与生成
def primitive_polynomial():
    min = pow(2, 8)
    max = pow(2, 9)
    for i in range(min, max):
        n = 8
        flag = 0
        if identity(i) and GCD_normal(i, pow(2, pow(2, n) - 1) + 1) == i:
            flag = 1
            for j in range(pow(2, n) - 1):
                if GCD_normal(i, pow(2, j) + 1) == i:
                    flag = 0
        if flag == 1:
            print('{:09b}'.format(i),end=' ')


if __name__ == '__main__':
    primitive_polynomial()
