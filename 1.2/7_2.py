def capitalize(s):
    isSpace = True
    result = ""
    result_1 = ""
    for i in s:
        if isSpace:
            result += i.upper()
            isSpace = False
        elif not isSpace:
            result += i.lower()
            isSpace = True
    isSpace = False
    for i in s:
        if isSpace:
            result_1 += i.upper()
            isSpace = False
        elif not isSpace:
            result_1 += i.lower()
            isSpace = True
    return [result, result_1]