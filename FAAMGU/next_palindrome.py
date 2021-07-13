
def next_palindrome(num):
    length = len(num)
    num = num
    carry = 0
    mid = length//2
    i, j = mid, mid

    if length % 2 == 0:
        i = mid-1

    if num[i] == 9:
        carry = 1
        num[i] = 0
        if i != j :
            num[j] = 0
    else:
        num[i] += 1
        if i != j:
            num[j] += 1
    i -= 1
    j += 1

    # print(num)
    while i >= 0:
        # print(num, i, carry)
        if carry == 1:
            if num[i] == 9:
                num[i] = 0
                num[j] = 0
            else:
                num[i] += 1
                num[j] += 1
                carry = 0

        i -= 1
        j += 1

    if carry == 1:
        num.append(1)
        num[0] = 1

    return num 
            

# print(next_palindrome([9,9,9]))
n = [[8], [9], [1,1], [1,8,1], [1,9,1], [9,9,9], [1,2,9,2,1], [1,2,3,3,2,1], [1,2,9,9,2,1]]
for i in n:
    print(next_palindrome(i))


