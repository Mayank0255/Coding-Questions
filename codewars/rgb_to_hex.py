def rgb(r, g, b):
    s = '%02x%02x%02x' % (clamp(r), clamp(g), clamp(b))
    return s.upper()

def clamp(x):
    return max(0, min(x, 255))
