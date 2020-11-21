def scramble(s1, s2):
    for letter in set(s2):
        if s1.count(letter) < s2.count(letter):
            return False
    return True
