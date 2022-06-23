def color_invert(rgb):
    r = abs(255 - rgb[0])
    g = abs(255 - rgb[1])
    b = abs(255 - rgb[2])

    return (r, g, b)


print(color_invert((255, 255, 255)))
print(color_invert((0, 0, 0)))
print(color_invert((165, 170, 221)))
