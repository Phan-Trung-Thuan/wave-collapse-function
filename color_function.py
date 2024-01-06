import random

def randomColor():
    r = random.randint(0, 255)        
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def darkerColor(rgb, factor):
    r, g, b = rgb
    r = max(0, int(r - factor))
    g = max(0, int(g - factor))
    b = max(0, int(b - factor))
    return (r, g, b)

def lighterColor(rgb, factor):
    r, g, b = rgb
    r = min(255, int(r + factor))
    g = min(255, int(g + factor))
    b = min(255, int(b + factor))
    return (r, g, b)