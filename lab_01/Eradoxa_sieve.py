def Eradoxa_sieve(N):
    if N < 2:
        return
    true_list = [True] * (N + 5)  # 其中 n 是你想要的 True 的个数
    for i in range(2, int(pow(N, 0.5))):
        if true_list[i]:
            k = i * i
            while k <= N:
                true_list[k] = False
                k = k + i
    for j in range(2, N + 1):
        if true_list[j]:
            print(j, end=' ')


# 测试
N = input()
Eradoxa_sieve(int(N))
