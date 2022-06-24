def probability(numbers_list, number):
    possibles = 0

    for n in numbers_list:
        if n >= number:
            possibles += 1

    return round(100 * (possibles / len(numbers_list)), 1)


print(probability([5, 1, 8, 9], 6))
print(probability([7, 4, 17, 14, 12, 3], 16))
print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))
