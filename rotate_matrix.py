from pprint import pprint

def translate(dy: int, dx: int, transform: list[list[tuple[int, int]]]) -> list[list[tuple[int, int]]]:
    print('-'*50, '[translate]')
    row, col = len(transform), len(transform[0])
    print(f'({row}, {col})')
    for r in range(row):
        for c in range(col):
            y, x = transform[r][c]
            transform[r][c] = [y+dy, x+dx]
    pprint(transform)
    return transform
            

def rotate_45(tranform: list[list[str]]) -> list[list[str]]:

    print('-'*50, '[rotate 45]')
    row, col = len(tranform), len(tranform[0])
    print(f'({row}, {col})')

    for r in range(row):
        for c in range(col):
            y, x = tranform[r][c]
            transform[r][c] = [y + c, x - r]

    pprint(transform)        
    return transform

def transform_fit(matrix, transform):
    nrow = len(matrix) + len(matrix[0]) - 1
    ncol = nrow
    new_matrix = list()
    for r in range(nrow):
        lst = list()
        for c in range(ncol):
            lst.append(' ')
        new_matrix.append(lst)

    for r in range(len(transform)):
        for c in range(len(transform[0])):
            y, x = transform[r][c]
            new_matrix[y][x] = matrix[r][c]

    pprint(new_matrix)
    return new_matrix

def strip_matrix(matrix: list[list[str]], rowcol: tuple[int, int]) -> list[list[str]]:

    print('-'*50, len(matrix), rowcol)

    row, col = len(matrix), len(matrix[0])
    while row:
        if ''.join(matrix[row-1]).strip() == '':
            matrix.pop() 
        row -= 1
    pprint(matrix)
    return

def print_matrix(matrix):
    for r in range(len(matrix)):
        print(''.join(matrix[r]))
    return

# Example usage
# matrix = [
#     ['d', 'a', 'm', 'i', 'r'],
#     ['m', 'a', 'r', 'k', 'o'],
#     ['d', 'a', 'r', 'k', 'o'],
# ]

matrix = [
    'damir',
    'marko',
    'darko'
]
row, col = len(matrix), len(matrix[0])
transform = list()
for r in range(row):
    lst = list()
    for c in range(col):
        lst.append([r,c])
    transform.append(lst)
print('='*50, '[init]')
print(f'({row}, {col})')
pprint(transform)
# print(matrix_rowcol)
transform = rotate_45(transform)
# tranform  = translate(0, row - 1, transform)
new_matrix = transform_fit(matrix, transform)
tranform = rotate_45(transform)
new_matrix = transform_fit(new_matrix, transform)

# matrix = rotate_45(matrix)
# matrix = rotate_45(matrix)
# tranform = rotate_45(transform)
# tranform  = translate(2, 1, transform)


# strip_matrix(rotated_matrix, matrix_rowcol)


# for r in range(len(rotated_matrix)):
#     print(''.join(rotated_matrix[r]).strip())