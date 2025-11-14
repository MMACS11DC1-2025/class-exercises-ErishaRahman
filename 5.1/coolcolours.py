def colour(r, g, b):
    if r <= 24 and g >= 230 and b <= 24:
        return ("green")
    if r <= 24 and g <= 24 and b >= 230:
        return ("blue")
    if r >= 230 and g <= 24 and b <= 24:
        return ("red")