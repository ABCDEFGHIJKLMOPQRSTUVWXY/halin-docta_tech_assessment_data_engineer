#kmp
def getNextVal(pattern):
    n = len(pattern)
    nextlist = [-1]
    i = 0
    j = -1
    while i < n-1:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            nextlist.append(j)
            if pattern[i] == pattern[j]:
                nextlist[i] = nextlist[j]
        else:
            j = nextlist[j]
    return nextlist

def KMP(target, pattern):
    t_len = len(target)
    p_len = len(pattern)
    i = 0
    j = 0
    nextlist = getNextVal(pattern)
    while i < t_len and j < p_len:
        if j == -1 or target[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = nextlist[j]
    if j == p_len:
        return i-p_len
    return -1