def find_outlier(integers):
    if integers[0] % 2 == 0 and integers[1] % 2 == 0:
        isEven = True
    elif integers[0] % 2 == 1 and integers[1] % 2 == 1:
        isEven = False
    else:
        if integers[2] % 2 == 0:
            isEven = True
        else:
            isEven = False
    for num in integers:
        if isEven and num % 2 == 1:
            return num
        elif not isEven and num % 2 == 0:
            return num
    return None
