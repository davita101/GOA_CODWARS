def min_sum(lst):
    lst.sort()
    mid = len(lst) // 2
    mini = lst[:mid]
    maxi = lst[mid:]
    summmer = []
    for i in range(len(mini)):
        summmer.append(mini[i] * maxi[len(maxi) - i - 1])
    return sum(summmer)