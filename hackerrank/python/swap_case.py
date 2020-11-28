def swap_case(s):
    return "".join([i.upper() if i.isupper() == False else i.lower() for i in s])
