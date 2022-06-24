def is_plural(word):
    return word[-1] == "s"


print(is_plural("changes"))
print(is_plural("change"))
print(is_plural("dudes"))
print(is_plural("magic"))
