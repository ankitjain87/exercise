def sum_n(n):
    cache = [0] * (n+1)

    for i in range(1, n+1):
        cache[i] = cache[i-1] + i

    return cache[n]


print(sum_n(1010101))