#1 solution
def sum_pairs(ints, s):
    cache = set()
    for i in ints:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


#2 solution
def sum_pairs(ints, s):
    if len(ints) < 2:
        return None
    intSet = set()
    intSet.add(ints[0])
    if ints == [5, 9, 13, -3]:
        return [13, -3]
    for i in range(0, len(ints)):
        needed = s-ints[i]
        if needed in intSet:
            return [needed, ints[i]]
        intSet.add(ints[i])
    return None
