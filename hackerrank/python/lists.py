if __name__ == '__main__':
    N = int(input())
    l = []

    while N != 0:
        instruction = input().split()
        if instruction[0] == 'insert':
            l.insert(int(instruction[1]), int(instruction[2]))
        elif instruction[0] == 'print':
            print(l)
        elif instruction[0] == 'remove':
            l.remove(int(instruction[1]))
        elif instruction[0] == 'append':
            l.append(int(instruction[1]))
        elif instruction[0] == 'sort':
            l.sort()
        elif instruction[0] == 'pop':
            l.pop()
        elif instruction[0] == 'reverse':
            l.reverse()
        N-=1
