if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    a = list()
    def find_coordinates(x, y, z, n):
        return [(i, j, k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

    coordinates = find_coordinates(x, y, z, n)
    for coord in coordinates:
        a.append(list(coord))
        
    print(a)    