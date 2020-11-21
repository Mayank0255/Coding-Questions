def valid_parentheses(string):
    stack = []
    if not string:
        return True

    for symbol in string:
        if symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            if len(stack) > 0:
                if symbol == ')' and stack[-1] == '(':
                    stack.pop()
            else:
                return False

    if not stack:
        return True
    else:
        return False
