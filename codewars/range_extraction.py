def solution(lst):
    res = []
    if lst:
        tmp, i, ln = lst[0], 0, len(lst)
        while i < ln:
            tmp, j = lst[i], i
            while j < ln - 1 and lst[j+1] == lst[j]+1:
                j += 1
            if j - i > 1:
                tmp = str(lst[i]) + "-" + str(lst[j])
                i = j+1
            else:
                i = (j if j > i else i+1)
            res.append(tmp)
    return ",".join(str(x) for x in res)
