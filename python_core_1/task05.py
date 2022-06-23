def priority_sort(unsort_lst, pri_set):
    pri_set_new = list(pri_set)
    remaining = sorted([i for i in unsort_lst if not i in pri_set_new])
    pri_list = []
    occur = {}

    if unsort_lst == []:
        return []

    for i in unsort_lst:
        occur[i] = occur.get(i, 0) + 1

    for i in pri_set_new:
        if i not in unsort_lst:
            pri_set_new.remove(i)
            continue

        for duplicates in range(occur[i]):
            pri_list.append(i)

    return pri_list + remaining


# print(priority_sort([5, 4, 3, 2, 1], {2, 3}))
print(priority_sort([5, 4, 3, 2, 1], {3, 6}))
print(priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}))
print(priority_sort([1, 5, 5, 5, 5, 2, 1], {1, 5}))  # [1, 1, 5, 5, 5, 5, 2]
assert priority_sort([1, 5, 5, 5, 5, 2, 1], {1, 5}) == [1, 1, 5, 5, 5, 5, 2]
