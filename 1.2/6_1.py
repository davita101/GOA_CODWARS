def parts_sums(ls):
    total_sum = sum(ls)
    result = [total_sum]
    for i in ls:
        total_sum -= i
        result.append(total_sum)
    return result