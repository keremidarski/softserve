def identical_filter(words):
    identicals = []

    for word in words:
        char_occur = {}

        for char in word:
            char_occur[char] = char_occur.get(char, 0) + 1

        if len(char_occur) == 1:
            identicals.append(word)

    return identicals


print(identical_filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"]))
