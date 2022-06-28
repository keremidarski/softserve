def sum_even_nums_in_range(start, stop):
    sum = 0

    for n in range(start, stop + 1):
        if n % 2 == 0:
            sum += n

    return sum


print(sum_even_nums_in_range(63, 97))
