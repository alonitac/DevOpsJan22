def bad_average(a, b, c):
    num = (a, b, c)
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg