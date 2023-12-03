def generate_pascals_triangle(rows):
    triangle = [[1]]
    for _ in range(1, rows):
        row = [1]
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j-1] + triangle[-1][j])
        row.append(1)
        triangle.append(row)
    for row in triangle:
        print(row)
n=int(input("Enter a digit"))
generate_pascals_triangle(n)
