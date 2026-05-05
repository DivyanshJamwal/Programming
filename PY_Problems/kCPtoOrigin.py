def k_closest(points, k):
    distances = [(x**2 + y**2, [x, y]) for x, y in points]
    
    distances.sort(key=lambda x: x[0])
    result = [point for _, point in distances[:k]]
    
    return result