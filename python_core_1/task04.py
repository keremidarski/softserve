def validate_subsets(subsets, one_set):
    for subset in subsets:
        for num in subset:
            if num not in one_set:
                return False

    return True


print(validate_subsets([[1, 2, 3, 4]], [1, 2, 3]))
