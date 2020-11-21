def spin_words(sentence):
    lst = sentence.split()

    for el in range(0, len(lst)):
        if len(lst[el]) >= 5:
            lst[el] = lst[el][::-1]
    return ' '.join(lst)
