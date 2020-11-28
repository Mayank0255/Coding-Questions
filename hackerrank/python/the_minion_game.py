def minion_game(string):
    string = string.lower()
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print(f"Kevin {kevsc}")
    elif kevsc < stusc:
        print(f"Stuart {stusc}")
    else:
        print("Draw")
