def average(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + average(lst[1:])


lst = [1, 2, 3, 4, 5]
print(average(lst)/len(lst))
