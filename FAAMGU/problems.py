import operator

# Given a non-empty array of integers, return the k most frequent elements.
def topKFrequent(nums, k):
    count = {}
    output = []
    for i in nums:
        if i not in count:
            count[i] = 0
        count[i] += 1

    sorted_count = sorted(count.items(), key=operator.itemgetter(1))
    for i in range(k):
        output.append(sorted_count[-i-1][0])

    return output


# print(topKFrequent([1,1,1,2,2,3], 2))
# print(topKFrequent([1], 1))



def plusOne(digits):
    all_nine = True
    for i in digits:
        if i != 9:
            all_nine = False
    if all_nine:
        return [1] + [0] * len(digits)

    carry = 1
    for i in range(len(digits)-1, -1, -1):
        if carry == 0:
            break
        n = digits[i] + carry
        if n > 9:
            digits[i], carry = 0, 1
        else:
            digits[i], carry = n, 0
    
    return digits

print(plusOne([9, 9, 9, 9]))