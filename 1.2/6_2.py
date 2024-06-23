def sum_consecutives(lst):
    arr = []
    summer = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == lst[i -1]:
            summer += lst[i]
        else:
            arr.append(summer)
            summer = lst[i]
            
    arr.append(summer)
    return arr