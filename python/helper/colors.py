def rgba_to_hsva(r, g, b, a):
    r *= (1 / 255)
    g *= (1 / 255)
    b *= (1 / 255)
    a *= (1 / 255)
    return r, g, b, a


def rgb_to_hsva(r, g, b):
    return rgba_to_hsva(r, g, b, 255)


name = {
    'dracula_dark': rgb_to_hsva(33, 34, 44),
    'dracula': rgb_to_hsva(93, 107, 153),
    'dracula_light': rgb_to_hsva(153, 163, 193),
}
