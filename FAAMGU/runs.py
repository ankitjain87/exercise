# 3

# 1,1,1
# 1,2
# 2,1
# 3

# -> 1,2,3,4

# 1 2 3 ...n 
# 1 2 
# def n_sum():
#     runs = [1,2,3,4]
#     dp = [1] * (n+1)
#     dp[0] = 1
#     dp[1] = 1

#     for i in range(2, n):  #        i = 2, 3, 4
#         for j in range(1, i):    #  j = 1, 1, 2
#             for r in runs:       #  r = 1
#                 if r <= i-j:
#                     dp[i] += dp[i-j]   

#     return dp[n]



# dp = [1, 1, 2 ]

# dp[3] = 1 + 2 + 1

# dp = [1, 1, ]


# nth step => sum (n-1) + (n-2) + (n-3) + (n-4) => N
def n_runs(n):
    runs = [1,2,3,4]
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        for r in runs:  
            if i-r >= 0:
                dp[i] += dp[i-r]

    return dp[n]


# i = 2, 3  4
# r = 1, 2, 3

# dp[2] = 1+1 => 2
# dp[3] = 2 + 1 + 1 = 4
# dp[4] = 4 + 2 + 1 + 1 => 8
# dp[5] = 8 + 4 + 2 + 1 => 15
print(n_runs(8), n_runs(9), n_runs(10))
