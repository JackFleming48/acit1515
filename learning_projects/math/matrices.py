import sys

def get_matrix():
    matrix = []
    matrix_in = input("Enter 'a' to add to the matrix. Enter 's' to stop adding rows: ")
    if matrix_in == 'a':
            matrix_row = input("How many rows will this matrix have: ")
            matrix_column = input("How many columns will this matrix have: ")
            count_col = 1
            count_row = 1
            entry = []
            for x in range(int(matrix_column)):
                 if count_col < x:
                      row_val = input(f"Enter the value for row {count_row}, column {count_col}: ")
                      entry.append(row_val)
                      count_col += 1
                 
    print(entry)
    

    if matrix_in == 's':
         print(matrix)
         sys.exit()
        


    

get_matrix()