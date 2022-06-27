def tallest_skyscraper(sky_list):
    for index, level in enumerate(sky_list):
        if 1 in level:
            return len(sky_list) - index


print(tallest_skyscraper([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]) == 3)
print(tallest_skyscraper([[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]) == 4)
print(tallest_skyscraper([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]) == 2)
