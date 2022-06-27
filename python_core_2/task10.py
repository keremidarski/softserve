def mineral_formation(stones):
    if 1 in stones[0] and 1 in stones[-1]:
        return "both"
    elif 1 in stones[0]:
        return "stalactites"
    elif 1 in stones[-1]:
        return "stalagmites"


print(
    mineral_formation([[0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]])
    == "stalactites"
)

print(
    mineral_formation([[0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]])
    == "stalagmites"
)

print(
    mineral_formation([[1, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 1]])
    == "both"
)
