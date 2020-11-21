def anagrams(word, words):
    res = []
    for el in words:
        elementLen = len(el)
        if len(word) == elementLen:
            check = [i for i in word]
            check.sort()
            checkWith = [i for i in el]
            checkWith.sort()
            if check == checkWith:
                res.append(el)
    return res
