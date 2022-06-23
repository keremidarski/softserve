def check(dict1, dict2, key_ch):
    if key_ch not in dict1 or key_ch not in dict2:
        return "One's empty"

    if dict1[key_ch] != dict2[key_ch]:
        return "Not the same"

    return True


dict_first = {
    "sky": "temple",
    "horde": "orcs",
    "people": 12,
    "story": "fine",
    "sun": "bright",
}
dict_second = {"people": 12, "sun": "star", "book": "bad"}

print(check(dict_first, dict_second, "horde"))
print(check(dict_first, dict_second, "people"))
print(check(dict_first, dict_second, "sun"))
