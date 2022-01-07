import math
def circle(a, b, r, edges):
    alfa = 0
    addon = 2 * math.pi / edges
    results = []
    for x in range(edges):
        results.append(math.sin(alfa) * r + a)
        results.append(math.cos(alfa) * r + b)
        results.append(0.0)
        alfa += addon
    return results