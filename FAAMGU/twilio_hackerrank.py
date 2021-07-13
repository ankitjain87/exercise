def firstOccurrence(s, x):
    if len(s) < len(x):
        return -1

    first = -1
    i, j = 0, 0
    while i < len(s):
        if x[j] == "*" or s[i] == x[j]:
            first = i
            start = i
            while j < len(x):
                if x[j] == "*" or s[start] == x[j]:
                    start += 1
                    j += 1
                else:
                    break
            if j == len(x):
                return first

            first = -1
            j = 0
        
        i += 1

    return first


# s = "juliasamathantha"
# x = "ant*a"
# print(firstOccurrence(s, x))


def processLogs(logs, threshold):
    user_dict = {}
    for log in logs:
        row = log.split(" ")
        if row[0] == row[1]:
            if row[0] not in user_dict:
                user_dict[row[0]] = 0   
            user_dict[row[0]] += 1
        else:
            for i in row[:2]:
                if i not in user_dict:
                    user_dict[i] = 0
                user_dict[i] += 1

    print(user_dict)
    thresh = []
    for k, v in user_dict.items():
        if v >= threshold:
            thresh.append(int(k))

    return map(str, sorted(thresh))




# logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
# threshold = 2
# print(processLogs(logs, threshold))

from collections import OrderedDict
filename = input()
timestamp_dict = OrderedDict()
with open(filename) as f:
    for line in f.readlines():
        t = line.strip().split("[")[1].split(" ")
        if t not in timestamp_dict:
            timestamp_dict[t] = 1
        else:
            timestamp_dict[t] += 1

new_file = 'req_' + filename
with open(new_file, "w") as f:
    for key, val in timestamp_dict.items():
        if val > 1:
            f.write(key)
            f.write("/n")

return new_file



[[-3,-2,2,3],[-2,-1,0,3],[-3,0,2,1],[-2,-1,1,2],[-2,0,0,2],[-3,-1,1,3],[-3,0,1,2],[-1,0,1,0],[-3,-2,3,2],[-2,0,2,0],[-2,-1,2,1],[-1,0,0,1],[-2,-1,3,0],[-3,-1,3,1],[-3,0,3,0],[-3,0,0,3]]