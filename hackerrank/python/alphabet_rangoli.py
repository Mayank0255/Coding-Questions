def print_rangoli(size):
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]

    for i in range(size-1, -size, -1):
        x = abs(i)
        line = myStr[size:x:-1]+myStr[x:size]
        print ("--"*x+ '-'.join(line)+"--"*x)
