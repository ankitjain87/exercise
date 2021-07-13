result = []
def permute(s, i, l):
    if i == l:
        result.append("".join(s))

    for j in range(i, l):
        s[i], s[j] = s[j], s[i]
        permute(s, i+1, l)
        s[i], s[j] = s[j], s[i]

permute(list("abcd"), 0, 4)
print(result, len(result))