def nearest_sq(n):
    root = int(n ** .5)
    
    sq_root = root ** 2
    sq_root_one = (root + 1) ** 2
    
    if abs(n - sq_root) <= abs(n - sq_root_one):
        return sq_root
    else:
        return sq_root_one