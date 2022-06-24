def filter_list(list_with_str_int):
    integers = []

    for i in list_with_str_int:
        if type(i) == int:
            integers.append(i)

    return integers


print(filter_list([1, 2, 3, "a", "b", 4]))
print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]))
print(filter_list(["Nothing", "here"]))
