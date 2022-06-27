def nth_smallest(list_numbers, ind_num):
    sorted_numbers = sorted(list_numbers)

    try:
        return sorted_numbers[ind_num - 1]
    except IndexError:
        return None


print(nth_smallest([1, 3, 5, 7], 1) == 1)
print(nth_smallest([1, 3, 5, 7], 3) == 5)
print(nth_smallest([1, 3, 5, 7], 5) == None)
print(nth_smallest([7, 3, 5, 1], 2) == 3)
