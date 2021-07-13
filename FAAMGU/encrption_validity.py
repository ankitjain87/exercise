from collections import Counter

def encryption_validty(instructionsCount, validityPeriod, keys):
    keys_counter = Counter(keys)
    max_divisor, key = 1, keys[0]
    # print(keys_counter)
    for k, v in keys_counter.items():
        count = 0
        for ki in list(keys_counter.keys()):
            # print(k, ki, count)
            if k == ki:
                count += v
            elif k % ki == 0:
                count += keys_counter[ki]

        if count > max_divisor:
            max_divisor = count
            key = k

    # print(key, max_divisor)
    degree = max_divisor * 10**5
    hijacker_test = instructionsCount * validityPeriod
    if hijacker_test >= degree:
        return [1, degree]
    
    return [0, degree]


print(encryption_validty(1000, 10000, [2,4,8,2,16]))


def numberGame(number):
    n = len(number)
    n2 = len(set(number))
    
    is_odd = (n - n2) % 2 == 1
    
    return n2 - int(is_odd)


print(numberGame([1,2,2,4,4]))