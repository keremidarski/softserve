def pops(pop_list):
    balloon_index = 0
    running_value = 0

    for index, value in enumerate(pop_list):
        if value > 0:
            balloon_index = index
            running_value = value - 1
            break

    r = balloon_index + 1
    l = balloon_index - 1

    for i in range(running_value):
        pop_list[r] = running_value
        pop_list[l] = running_value
        r += 1
        l -= 1
        running_value -= 1

    return pop_list


print(pops([0, 0, 0, 0, 4, 0, 0, 0, 0]) == [0, 1, 2, 3, 4, 3, 2, 1, 0])
print(pops([0, 0, 0, 3, 0, 0, 0]) == [0, 1, 2, 3, 2, 1, 0])
print(pops([0, 0, 2, 0, 0]) == [0, 1, 2, 1, 0])
print(pops([0]) == [0])
