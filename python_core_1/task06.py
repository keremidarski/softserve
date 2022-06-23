def len_longest_chain(chain_pairs):
    sorted_chain = sorted(chain_pairs)
    max_streak = 1

    for pair in sorted_chain:
        last_number = pair[1]
        counter = 1

        for second_pair in sorted_chain:
            start = second_pair[0]
            end = second_pair[1]

            if start > last_number:
                counter += 1
                last_number = end
            else:
                continue

        if counter > max_streak:
            max_streak = counter

    return max_streak


print(len_longest_chain([(2, 3), (3, 4), (3, 5)]))
print(len_longest_chain([(2, 3), (3, 4), (1, 2)]))
print(len_longest_chain([(-15, -11), (17, 22), (8, 12), (-11, -10), (-4, -1)]))
print(len_longest_chain([(-5, 0), (-4, 0), (4, 5), (3, 4), (-1, 1), (-6, -2)]))
