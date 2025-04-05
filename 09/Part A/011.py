def create_list(list1, list2):
    return [x for x in list1 if x in list2]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(create_list(list1, list2))
