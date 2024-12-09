import re
import numpy as np

def main(file):

    xmas = r"XMAS"
    samx = r"SAMX"
    mas = r"MAS"
    sam = r"SAM"
    
    # Count horizontal forward
    matches_horizontal_forward = re.findall(xmas, file, flags=re.DOTALL)

    # Count horizontal backwards
    matches_horizontal_backwards = re.findall(samx, file, flags=re.DOTALL)

    # Transpose
    lines = list(file.split("\n"))
    matrix = [list(line) for line in lines]
    transposed = list(zip(*matrix))
    list_file_transposed = ["".join(row) for row in transposed]
    file_transposed = "\n".join(list_file_transposed)
    
    # Count vertical forwards
    matches_vertical_forward = re.findall(xmas, file_transposed, flags=re.DOTALL)
    
    # Count vertical backwards
    matches_vertical_backwards = re.findall(samx, file_transposed, flags=re.DOTALL)
    
    # Diagonal (using numpy)
    np_matrix = np.array(matrix)
    diags = [np_matrix[::-1,:].diagonal(i) for i in range(-np_matrix.shape[0]+1,np_matrix.shape[1])]
    diags.extend(np_matrix.diagonal(i) for i in range(np_matrix.shape[1]-1,-np_matrix.shape[0],-1))

    list_diagonal = [n.tolist() for n in diags]
    list_text_diagonal = ["".join(row) for row in list_diagonal]
    text_diagonal = "\n".join(list_text_diagonal)
    
    # Diagonal forwards 
    matches_diagonal_forward = re.findall(xmas, text_diagonal, flags=re.DOTALL)
    
    # Diagonal backwards
    matches_diagonal_backward = re.findall(samx, text_diagonal, flags=re.DOTALL)
    
    total_matches = len(matches_horizontal_forward) + len(matches_horizontal_backwards) + len(matches_vertical_forward) + len(matches_vertical_backwards) + len(matches_diagonal_forward) + len(matches_diagonal_backward)
    print(total_matches)
    
    # PART 2 
    
    # Search for X-MAS
    # Search for the "A" and then get its diagonal neighborrs
    
    a_locations = np.argwhere(np_matrix == "A")
    
    diagonal_neighbors = []
    for a in a_locations:
        diagonal_neighbors.append(get_diagonal_neighbors(np_matrix, a[0], a[1]))

    diagonal_neighbors = [item for item in diagonal_neighbors if item != None]

    total_x_mas = get_valid_x_mas(np_matrix, diagonal_neighbors)
    print(total_x_mas)

def get_diagonal_neighbors(matrix, x, y):
    
    rows, cols = matrix.shape  # Dimensiones de la matriz
    
    diagonals = [
        (x - 1, y - 1),  # Superior izquierda
        (x - 1, y + 1),  # Superior derecha
        (x + 1, y - 1),  # Inferior izquierda
        (x + 1, y + 1)   # Inferior derecha
    ]
    
    valid_diagonals = [
        (i, j) for i, j in diagonals if 0 <= i < rows and 0 <= j < cols
    ]

    if (len(valid_diagonals) == 4):
        return valid_diagonals
    else:
        return
    
def get_valid_x_mas(matrix, diagonal_neighbors):
    total = 0
    for i, j, k, l in diagonal_neighbors:
        if (((matrix[i] == "M" and matrix[l] == "S") or (matrix[i] == "S" and matrix[l] == "M")) and ((matrix[j] == "M" and matrix[k] == "S") or (matrix[j] == "S" and matrix[k] == "M"))):
            total += 1
            
    return total
    
if __name__ == "__main__":
    file = open("test.txt", "r")
    file = open("input.txt", "r")
    # lines = file.read().split("\n")
    main(file.read())
