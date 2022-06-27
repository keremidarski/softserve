def count_overlapping(list_intervals, point):
    overlaps = 0

    for interval in list_intervals:
        if interval[0] <= point <= interval[1]:
            overlaps += 1

    return overlaps


print(count_overlapping([[1, 2], [2, 3], [3, 4]], 5) == 0)
print(count_overlapping([[1, 2], [5, 6], [5, 7]], 5) == 2)
print(count_overlapping([[1, 2], [5, 8], [6, 9]], 7) == 2)
