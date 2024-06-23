def generate_hashtag(s):
    #your code here
    
    arr = "#" +"".join([char.capitalize() for char in s.split()])
    if len(arr) > 140 :
        return 0
    elif s == '':
        return 0
    return arr