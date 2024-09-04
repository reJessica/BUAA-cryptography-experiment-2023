import random


def GCD_normal(a, b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % b
    else:
        return abs(a)


def decomposition_of_a_composite_number(e, d, n):
    while True:
        k = e * d - 1
        g = random.randint(0, n)
        while k % 2 == 0:
            k = k // 2
            temp = pow(g, k, n) - 1
            if GCD_normal(temp, n) > 1 and temp != 0:
                return GCD_normal(temp, n)


def main():
    e = int(input())
    d = int(input())
    n = int(input())
    result1 = decomposition_of_a_composite_number(e, d, n)
    result2 = n // result1
    # 按照大小顺序输出
    sorted_list = sorted([result1, result2])
    for num in sorted_list:
        print(num)


if __name__ == "__main__":
    main()
