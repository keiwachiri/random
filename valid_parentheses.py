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


def valid_braces(string):
    # TODO - refactor to use dictionary and stack
    count_parentheses = count_brackets = count_braces = 0
    for char in string:
        if char == '(':
            count_parentheses += 1
        elif char == ')':
            count_parentheses -= 1
        elif char == '[':
            count_brackets += 1
        elif char == ']':
            count_brackets -= 1
        elif char == '{':
            count_braces += 1
        elif char == '}':
            count_braces -= 1
        if count_brackets < 0 or count_parentheses < 0 or count_braces < 0:
            return False
    if (count_brackets, count_parentheses, count_braces) != (0, 0, 0):
        return False
    else:
        return True
