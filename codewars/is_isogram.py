def is_isogram(string):
    string = string.lower()
    for ltr in string:
        if string.count(ltr) > 1:
            return False
    return True
