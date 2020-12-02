"""Framework for Solving DP Problems:
	1. Define the objective function
		f(i) is the number of distinct ways to reach the i-th stair.
	2. Identify base cases
		f(0) = 1
		f(1) = 1
	3. Write down a recurrence relation for the optimized objective function
		f(n) = f(n-1) + f(n-2)
	4. What's the order of execution?
		bottom-up
	5. Where to look for the answer?
		f(n)
"""


def stair_case(n):
    "F(n) = F(n-1) + F(n-2)"

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# Optimized space
def stair_case2(n):
    a = 1
    b = 1

    for i in range(2, n+1):
        c = a + b
        a = b
        b = c

    return b



# print(stair_case2(10))
# print(stair_case(10))


def stair_case_3_steps(n):
    """Framework for Solving DP Problems:
	1. Define the objective function
		f(i) is the number of distinct ways to reach the i-th stair.
	2. Identify base cases
		f(0) = 1
		f(1) = 1
        f(2) = 2
	3. Write down a recurrence relation for the optimized objective function
		f(n) = f(n-1) + f(n-2) + f(n-3)
	4. What's the order of execution?
		bottom-up
	5. Where to look for the answer?
		f(n)
"""
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]


# print(stair_case_3_steps(10))


def stair_case_k_steps(n, k):
    """Framework for Solving DP Problems:
	1. Define the objective function
		f(i) is the number of distinct ways to reach the i-th stair.
	2. Identify base cases
		f(0) = 1
		f(1) = 1
	3. Write down a recurrence relation for the optimized objective function
		f(n) = f(n-1) + f(n-2) + ..... + f(n-k)
	4. What's the order of execution?
		bottom-up
	5. Where to look for the answer?
		f(n)
    """
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        for j in range(1, k):
            if i >= j:
                dp[i] += dp[i-j]

    return dp[n]

# print(stair_case_k_steps(10, 3))


def climb_stair_case_k_steps_and_avoid_red_stairs(n, k, rs):
    """Framework for Solving DP Problems:
	1. Define the objective function
		f(i) is the number of distinct ways to reach the i-th stair.
	2. Identify base cases
		f(0) = 1
	3. Write down a recurrence relation for the optimized objective function
		f(n) = f(n-1) + f(n-2) + ..... + f(n-k)
	4. What's the order of execution?
		bottom-up
	5. Where to look for the answer?
		f(n)
    """
    dp = [0] * (k)
    dp[0] = 1 
    for i in range(1, n+1):
        for j in range(1, k):
            # Check if its a red stair
            if i -j < 0:
                continue

            if rs[i-1]:
                dp[i % k] = 0
            else:
                dp[i % k] += dp[(i-j) % k]

    return dp[n % k]


# print(climb_stair_case_k_steps_and_avoid_red_stairs(7, 3, [False, True, False, True, True, False, False]))

    
def climb_stair_min_cost(n, p):
    """Problem:
	Paid Staircase
	You are climbing a paid staircase. It takes n steps to reach to the top and you have to
	pay p[i] to step on the i-th stair. Each time you can climb 1 or 2 steps.
	What's the cheapest amount you have to pay to get to the top of the staircase?
    
    p = [0, 3, 2, 4]
    """

    """Framework for Solving DP Problems:
	1. Define the objective function
		f(i) is the number of distinct ways to reach the i-th stair.
	2. Identify base cases
		f(0) = 0
        f(1) = p[1]
	3. Write down a recurrence relation for the optimized objective function
		f(n) = P(n) + min(f(n-1), f(n-2))
	4. What's the order of execution?
		bottom-up
	5. Where to look for the answer?
		f(n)
    """
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = p[1]

    for i in range(2, n+1):
        dp[i] = p[i] + min(dp[i-1], dp[i-2])

    return dp[n]

# print(climb_stair_min_cost(3, [0, 3, 2, 4]))


def climb_stair_min_cost_path(n, p):
    dp = [0] * (n+1)
    from_path = [0] * (n+1)
    dp[0] = 0
    dp[1] = p[1]

    for i in range(1, n+1):
        dp[i] = p[i] + min(dp[i-1], dp[i-2])

        if dp[i-1] < dp[i-2]:
            from_path[i] = i-1
        else:
            from_path[i] = i-2

    path, curr = [], n
    while curr > 0:
        path.append(curr)
        curr = from_path[curr]

    path.append(0)
    path.reverse()
    return path
    
print(climb_stair_min_cost_path(8, [0, 3, 2, 4, 6, 1, 1, 5, 3]))