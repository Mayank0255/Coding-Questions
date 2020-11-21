def solution(string, markers):
    string = string.split('\n')
    res = []
    i = 0
    while i < len(string):
        gotIt = True
        j = 0
        while j < len(string[i]):
            if string[i][j] in markers:
                res.append(string[i][:j].strip())
                gotIt = False
                break
            j += 1
        if gotIt:
            res.append(string[i].strip())
        i += 1
    return '\n'.join(res)
