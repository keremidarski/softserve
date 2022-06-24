def index_of_caps(word):
    result = []

    for index, value in enumerate(word):
        if value.isupper():
            result.append(index)

    return sorted(result)


print(index_of_caps("eQuINoX"))
print(index_of_caps("determine"))
print(index_of_caps("STRIKE"))
print(index_of_caps("sUn"))
