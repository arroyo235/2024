import re
import numpy as np

def main(file):

    xmas = r"XMAS"
    samx = r"SAMX"
    
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
    
    
if __name__ == "__main__":
    file = open("test.txt", "r")
    file = open("input.txt", "r") # 2409 too low
    # lines = file.read().split("\n")
    main(file.read())
