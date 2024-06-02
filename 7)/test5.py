def rot13(m):
    lower_word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    upper_word = ''
    for i in lower_word:
        upper_word += i.upper()
    concat = lower_word + upper_word
    finnal_output = ''
    
    for char in m:
        if char in concat:
            finnal_output += concat[concat.index(char) + 13]
        else:
            finnal_output += char
            
    return finnal_output