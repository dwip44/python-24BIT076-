def create_array(x, y, z, n):
    return [[[n for _ in range(z)] for _ in range(y)] for _ in range(x)]


print(create_array(3, 4, 5, 0))
