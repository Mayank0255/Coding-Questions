def move_zeros(array):
    new = []
    zeros = []

    for i in range(len(array)):
        if array[i] == 0 or array[i] == 0.0:
            if type(array[i]) == int or type(array[i]) == float:
                zeros.append(array[i])
            else:
                new.append(array[i])
        else:
            new.append(array[i])

    return new + zeros
