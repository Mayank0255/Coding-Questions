import itertools

def next_bigger(n):
    l = len(str(n))
    flag = 0
    for i in reversed(range(0,l-1)) :
        c_value = str(n)[i]
        cand_list = list(str(n)[i+1:])

        min = 10
        min_idx = 10
        # to catch min
        for k in range(0,len(cand_list)):
            if int(c_value) < int(cand_list[k]) and int(min) > int(cand_list[k]) :
                if(min!= cand_list[k]):
                    min = cand_list[k]
                    min_idx = k

        if(min != 10) :
            tmp = c_value
            c_value = cand_list[min_idx]
            cand_list[min_idx] = tmp
            cand_list = sorted(map(int, cand_list))

            return int(str(n)[:i] + c_value + "".join(map(str,cand_list)))

    if flag == 0:
        return -1
