"""
    Constant Time solution O(1). 
    It should be a easy problem, the idea is to find the number contains 0, 1, so the max number in the given will be answer that many 1 0 combination number we need to add to the given number.
    """
def minPartitions(n):
    for i in range(9, -1, -1):
        if str(i) in n:
            return i

    return 0


# print(minPartitions("27346209830709182346"))


from collections import defaultdict
def next_num(nums):
    nums = [0,20,7,16,1,18,15]
    nums_dict = defaultdict(list)
    for i, val in enumerate(nums):
        nums_dict[val].append(i)

    i = len(nums)
    next_num = None
    last_num = 15
    while i < 30000000:
        if len(nums_dict[last_num]) == 1:
            next_num = 0
        else:
            temp = nums_dict[last_num]
            next_num = temp[-1] - temp[-2]

        last_num = next_num
        if len(nums_dict[next_num]) == 2:
            nums_dict[next_num] = [nums_dict[next_num][-1], i]
        else:
            nums_dict[next_num].append(i)
        i += 1

    print(last_num, len(nums_dict))

next_num([])