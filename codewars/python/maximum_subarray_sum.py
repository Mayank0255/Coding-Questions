def max_sequence(array):
    if len(array) == 0:
        return 0
    maxSoFar = array[0]
    maxEndingHere = array[0]
    for i in range(1, len(array)):
        maxEndingHere = max(array[i], maxEndingHere + array[i])
        maxSoFar = max(maxEndingHere, maxSoFar)
    return 0 if maxSoFar == -1 else maxSoFar
