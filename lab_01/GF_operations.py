def GF_operations(x, op, y):
    if op == '+':
        add = x ^ y
        return add
    elif op == '-':
        dim = x ^ y
        return dim
    elif op == '*':
        ans = 0
        while y > 0:
            if y & 1 == 1:
                ans ^= x
            x <<= 1
            if x & 0x100 == 0x100:
                x ^= 0x11b
            x &= 0xff
            y >>= 1
        return ans
    elif op == '/':
        if y == 1:
            return x, 0
        num1 = len(bin(x)[2:])
        num2 = len(bin(y)[2:])
        if num1 == num2:
            return 1, x ^ y
        elif num1 < num2:
            return 0, x
        else:
            ans = 0
            while num1 >= num2:
                rec = num1 - num2
                x ^= (y << rec)
                ans ^= (1 << rec)
                num1 = len(bin(x)[2:])
        return ans, x
    return -1


# 测试
X, Y, Z = input().split(" ")
x = int(X, 16)
z = int(Z, 16)
result = GF_operations(x, Y, z)
if type(result) == tuple:
    formatted_result = '{:02x} {:02x}'.format(result[0], result[1])
else:
    formatted_result = '{:02x}'.format(result)

print(formatted_result)