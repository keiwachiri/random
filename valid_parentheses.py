def valid_parentheses(string):
    count = 0
    for item in string:
        if item == '(':
            count += 1
        elif item == ')':
            count -= 1
        if count < 0:
            return False
    return True if count == 0 else False
