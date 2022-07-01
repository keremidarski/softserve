def show_the_love(share_list):
    smallest_value = 10000
    smallest_index = 0
    removed = 0

    for index, number in enumerate(share_list):
        if number < smallest_value:
            smallest_value = number
            smallest_index = index
    
    for index, number in enumerate(share_list):
        if number != smallest_value:
            removed += number * 0.25
            share_list[index] = number * 0.75

    share_list[smallest_index] += removed

    return share_list

print(show_the_love([4, 1, 4]) == [3, 3, 3])
print(show_the_love([16, 10, 8]) == [12, 7.5, 14.5])
print(show_the_love([2, 100]) == [27, 75])