def initialize_matrix():
    new_matrix = [
        [1,2,3,0],
        [1,2,3,0],
        [1,2,3,0],
        [0,0,0,0]
    ]

    return new_matrix


def transform_matrix(mtx):
    final_row = len(mtx) - 1

    final_column = len(mtx[0]) - 1
    
    elements_sum = 0

    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if i < final_row and j < final_column:
                mtx[i][final_column] += mtx[i][j]
                matrix[final_row][j] += mtx[i][j]
            elements_sum += mtx[i][j]
        
    mtx[final_row][final_column] = elements_sum
    
    return mtx

def print_matrix(mtx):
    for row in mtx:
        print(' '.join(list(map(str, row))))
        


matrix = initialize_matrix()
matrix = transform_matrix(matrix)
print_matrix(matrix)
