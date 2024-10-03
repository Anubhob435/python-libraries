import numpy as np

def matrix_input(prompt):
    rows = int(input(f"Enter the number of rows for {prompt}: "))
    cols = int(input(f"Enter the number of columns for {prompt}: "))
    print(f"Enter the elements for {prompt} row-wise:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

def add_matrices(A, B):
    return A + B

def subtract_matrices(A, B):
    return A - B

def multiply_matrices(A, B):
    return A @ B

def elementwise_division(A, B):
    return A / B

def matrix_inverse(A):
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return "Matrix is singular and cannot be inverted."

def matrix_transpose(A):
    return A.T

def matrix_rank(A):
    return np.linalg.matrix_rank(A)

def adjacency_matrix(A):
    # Create adjacency matrix from a given square matrix (for simplicity)
    return (A != 0).astype(int)

def matrix_calculator():
    print("Welcome to the Matrix Calculator!")
    print("Please select the operation:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Element-wise Division")
    print("5. Matrix Inverse")
    print("6. Matrix Transpose")
    print("7. Matrix Rank")
    print("8. Adjacency Matrix")
    print("")
    
    choice = input("Enter the operation number: ")

    if choice in ['1', '2', '3', '4']:
        A = matrix_input("Matrix A")
        B = matrix_input("Matrix B")
        if A.shape != B.shape and choice != '3':
            print("Error: Matrices must have the same dimensions for this operation.")
            return
    else:
        A = matrix_input("Matrix A")
    
    if choice == '1':
        result = add_matrices(A, B)
        print("Result of Addition:\n", result)
    elif choice == '2':
        result = subtract_matrices(A, B)
        print("Result of Subtraction:\n", result)
    elif choice == '3':
        if A.shape[1] != B.shape[0]:
            print("Error: Number of columns of Matrix A must equal the number of rows of Matrix B for multiplication.")
            return
        result = multiply_matrices(A, B)
        print("Result of Multiplication:\n", result)
    elif choice == '4':
        result = elementwise_division(A, B)
        print("Result of Element-wise Division:\n", result)
    elif choice == '5':
        result = matrix_inverse(A)
        print("Matrix Inverse:\n", result)
    elif choice == '6':
        result = matrix_transpose(A)
        print("Matrix Transpose:\n", result)
    elif choice == '7':
        result = matrix_rank(A)
        print(f"Matrix Rank: {result}")
    elif choice == '8':
        result = adjacency_matrix(A)
        print("Adjacency Matrix:\n", result)
    else:
        print("Invalid operation number!")

if __name__ == "__main__":
    matrix_calculator()
