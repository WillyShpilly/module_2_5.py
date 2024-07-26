def get_matrix(n, m, value):
    matrix = []
    for i in range (n):
        row = []
        for j in range (m):
            row.append(value)
        matrix.append(row)
    return matrix

result1 = get_matrix(n=2, m=2, value=10)
result2 = get_matrix(n=3, m=5, value=42)
result3 = get_matrix(n=4, m=2, value=13)

print(result1)
print(result2)
print(result3)