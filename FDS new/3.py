'''

Write a Python program to compute following computation on matrix:
a) Addition of two matrices
B) Subtraction of two matrices
c) Multiplication of two matrices
d) Transpose of a matrix

'''


def inputMatrix(rows, cols):

    mat = []
    for i in range(rows):
        mat.append([])
        for j in range(cols):
            mat[i].append(int(input(f'Value of {i},{j}: ')))
    return mat


def addMatrix(mat1, mat2):
    if (len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
        print("Matrix1 and Matrix2 have different number of rows and columns hence can't be added")
        return None
    mat = []
    for i in range(len(mat1)):
        mat.append([])
        for j in range(len(mat1[0])):
            mat[i].append(mat1[i][j] + mat2[i][j])
    return mat


def subtractMatrix(mat1, mat2):
    if (len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
        print("Matrix1 and Matrix2 have different number of rows and columns hence can't be subtracted")
        return None
    mat = []
    for i in range(len(mat1)):
        mat.append([])
        for j in range(len(mat1[0])):
            mat[i].append(mat1[i][j] - mat2[i][j])
    return mat


def transposeMatrix(mat):
    ans = []
    for j in range(len(mat[0])):
        ans.append([])
        for i in range(len(mat)):
            ans[j].append(mat[i][j])
    return ans


def multiplyMatrix(mat1, mat2):
    if(len(mat1[0]) != len(mat2)):
        print("Matrix can't be multiplied")
        return None
    ans = []
    for i in range(len(mat1)):
        ans.append([])
        for j in range(len(mat2[0])):
            sm = 0
            for same_idx in range(len(mat1[0])):
                sm += mat1[i][same_idx] * mat2[same_idx][j]
            ans[i].append(sm)

    return ans


def displayMatrix(mat):
    if(mat == None):
        print("Argument is not a matrix!")
        return
    for i in range(len(mat)):
        print("| ", end="")
        for j in range(len(mat[0])):
            print(str(mat[i][j]).zfill(3), end=" ")
        print("|")


def saddlePointMatrix(mat):
    for i in range(len(mat)):
        minimum = min(mat[i])
        for j in range(len(mat[0])):
            if mat[i][j] == minimum:
                breakFlag = False
                for row_index in range(len(mat)):
                    if mat[row_index][j] > mat[i][j]:
                        breakFlag = True
                        break
                if not breakFlag:
                    return mat[i][j]
    return None


print("Chose a option from menu:")
print("1) Input Matrix")
print("2) Add Matrix")
print("3) Subtract Matrix")
print("4) Multiply matrix")
print("5) Transpose of matrix")
print("6) Saddle point of matrix (PRACTICE PROBLEM)")

matrix1 = None
matrix2 = None
while (True):
    option = int(input("Menu Option: "))

    if option == 1:
        while (True):
            try:
                row1 = int(input("Number of row in 1st matrix: "))
                col1 = int(input("Number of columns in 1st matrix: "))
                row2 = int(input("Number of row in 2nd matrix: "))
                col2 = int(input("Number of columns in 2nd matrix: "))
                if(row1 < 1 or row2 < 1 or col1 < 1 or col2 < 1):
                    raise
                break
            except:
                print("Invalid Input. Please give valid input!")

        print("----Input For Matrix 1----")
        matrix1 = inputMatrix(row1, col1)
        print("----Input For Matrix 2----")
        matrix2 = inputMatrix(row2, col2)
    elif option > 1 and matrix1 == None or matrix2 == None:
        print("Please input matrix first!")
        continue
    elif option == 2:
        displayMatrix(addMatrix(matrix1, matrix2))
    elif option == 3:
        print("1) matrix1 - matrix2")
        print("2) matrix2 - matrix1")
        while(True):
            inner_option = int(input("Choose option: "))
            if(inner_option >= 1 and inner_option <= 2):
                break
            print("Invalid Input")
        displayMatrix(subtractMatrix(matrix1, matrix2)
                      if inner_option == 1 else subtractMatrix(matrix2, matrix1))
    elif option == 4:
        print("1) matrix1 * matrix2")
        print("2) matrix2 * matrix1")
        while(True):
            inner_option = int(input("Choose option: "))
            if(inner_option >= 1 and inner_option <= 2):
                break
            print("Invalid Input")
        displayMatrix(multiplyMatrix(matrix1, matrix2)
                      if inner_option == 1 else multiplyMatrix(matrix2, matrix1))
    elif option == 5:
        print("1) Transpose of matrix1")
        print("2) Transpose of matrix2")
        while(True):
            inner_option = int(input("Choose option: "))
            if(inner_option >= 1 and inner_option <= 2):
                break
            print("Invalid Input")
        displayMatrix(transposeMatrix(matrix1)
                      if inner_option == 1 else transposeMatrix(matrix2))
    elif option == 6:
        print("1) Saddle point of matrix1")
        print("2) Saddle point of matrix2")
        while(True):
            inner_option = int(input("Choose option: "))
            if(inner_option >= 1 and inner_option <= 2):
                break
            print("Invalid Input")
        ans = saddlePointMatrix(
            matrix1) if inner_option == 1 else saddlePointMatrix(matrix2)
        if ans != None:
            print("Saddle point is", ans)
        else:
            print("There is no saddle point")

    elif option == -1:
        break
    else:
        print("Invalid Input")


'''
Output 

---------------------------
Test case 1 - Invalid matrix size input
---------------------------

Chose a option from menu:
1) Input Matrix
2) Add Matrix
3) Subtract Matrix
4) Multiply matrix
5) Transpose of matrix
6) Saddle point of matrix (PRACTICE PROBLEM)
Menu Option: 1
Number of row in 1st matrix: -1
Number of columns in 1st matrix: -4
Number of row in 2nd matrix: -2
Number of columns in 2nd matrix: -1
Invalid Input. Please give valid input!
Number of row in 1st matrix:

---------------------------
Test Case 2 - Matrix 1 size (3 x 2) and Matrix 2 size (2 x 3)
---------------------------

Chose a option from menu:
1) Input Matrix
2) Add Matrix
3) Subtract Matrix
4) Multiply matrix
5) Transpose of matrix
6) Saddle point of matrix (PRACTICE PROBLEM)
Menu Option: 1
Number of row in 1st matrix: 3
Number of columns in 1st matrix: 2
Number of row in 2nd matrix: 2
Number of columns in 2nd matrix: 3
----Input For Matrix 1----
Value of 0,0: 1
Value of 0,1: 2
Value of 1,0: 3
Value of 1,1: 4
Value of 2,0: 5
Value of 2,1: 6
----Input For Matrix 2----
Value of 0,0: 4
Value of 0,1: 5
Value of 0,2: 6
Value of 1,0: 3
Value of 1,1: 4
Value of 1,2: 5
Menu Option: 2
Matrix1 and Matrix2 have different number of rows and columns hence can't be added
Argument is not a matrix!
Menu Option: 3
1) matrix1 - matrix2
2) matrix2 - matrix1
Choose option: 1
Matrix1 and Matrix2 have different number of rows and columns hence can't be subtracted
Argument is not a matrix!
Menu Option: 4
1) matrix1 * matrix2
2) matrix2 * matrix1
Choose option: 1
| 010 013 016 |
| 024 031 038 |
| 038 049 060 |
Menu Option: 4
1) matrix1 * matrix2
2) matrix2 * matrix1
Choose option: 2
| 049 064 |
| 040 052 |
Menu Option: 5
1) Transpose of matrix1
2) Transpose of matrix2
Choose option: 1
| 001 003 005 |
| 002 004 006 |
Menu Option: 5
1) Transpose of matrix1
2) Transpose of matrix2
Choose option: 2
| 004 003 |
| 005 004 |
| 006 005 |
Menu Option: 6
1) Saddle point of matrix1
2) Saddle point of matrix2
Choose option: 1
Saddle point is 5
Menu Option: 6
1) Saddle point of matrix1
2) Saddle point of matrix2
Choose option: 2
Saddle point is 4
Menu Option: -1

---------------------------
Test case 3 - Matrix 1 size (3 x 4) and Matrix 2 size (3 x 4)
---------------------------

Chose a option from menu:
1) Input Matrix
2) Add Matrix
3) Subtract Matrix
4) Multiply matrix
5) Transpose of matrix
6) Saddle point of matrix (PRACTICE PROBLEM)
Menu Option: 1
Number of row in 1st matrix: 3
Number of columns in 1st matrix: 4
Number of row in 2nd matrix: 3
Number of columns in 2nd matrix: 4
----Input For Matrix 1----
Value of 0,0: 1
Value of 0,1: -2
Value of 0,2: -5
Value of 0,3: 4
Value of 1,0: 33
Value of 1,1: 6
Value of 1,2: 5
Value of 1,3: 9
Value of 2,0: 8
Value of 2,1: -5
Value of 2,2: 44
Value of 2,3: 5
----Input For Matrix 2----
Value of 0,0: -3
Value of 0,1: -8
Value of 0,2: 4
Value of 0,3: 55
Value of 1,0: 33
Value of 1,1: 2
Value of 1,2: 33
Value of 1,3: 7
Value of 2,0: 6
Value of 2,1: -4
Value of 2,2: 2
Value of 2,3: 1
Menu Option: 2
| -02 -10 -01 059 |
| 066 008 038 016 |
| 014 -09 046 006 |
Menu Option: 3
1) matrix1 - matrix2
2) matrix2 - matrix1
Choose option: 1
| 004 006 -09 -51 |
| 000 004 -28 002 |
| 002 -01 042 004 |
Menu Option: 3
1) matrix1 - matrix2
2) matrix2 - matrix1
Choose option: 2
| -04 -06 009 051 |
| 000 -04 028 -02 |
| -02 001 -42 -04 |
Menu Option: 4
1) matrix1 * matrix2
2) matrix2 * matrix1
Choose option: 1
Matrix can't be multiplied
Argument is not a matrix!
Menu Option: 4
1) matrix1 * matrix2
2) matrix2 * matrix1
Choose option: 2
Matrix can't be multiplied
Argument is not a matrix!
Menu Option: 5
1) Transpose of matrix1
2) Transpose of matrix2
Choose option: 1
| 001 033 008 |
| -02 006 -05 |
| -05 005 044 |
| 004 009 005 |
Menu Option: 5
1) Transpose of matrix1
2) Transpose of matrix2
Choose option: 2
| -03 033 006 |
| -08 002 -04 |
| 004 033 002 |
| 055 007 001 |
Menu Option: 6
1) Saddle point of matrix1
2) Saddle point of matrix2
Choose option: 1
There is no saddle point
Menu Option: 6
1) Saddle point of matrix1
2) Saddle point of matrix2
Choose option: 2
Saddle point is 2
Menu Option: -1

---------------------------
Test case 4 - All Elements 0
---------------------------

Chose a option from menu:
1) Input Matrix
2) Add Matrix
3) Subtract Matrix
4) Multiply matrix
5) Transpose of matrix
6) Saddle point of matrix (PRACTICE PROBLEM)
Menu Option: 1
Number of row in 1st matrix: 2
Number of columns in 1st matrix: 2
Number of row in 2nd matrix: 2
Number of columns in 2nd matrix: 2
----Input For Matrix 1----
Value of 0,0: 0
Value of 0,1: 0
Value of 1,0: 0
Value of 1,1: 0
----Input For Matrix 2----
Value of 0,0: 0
Value of 0,1: 0
Value of 1,0: 0
Value of 1,1: 0
Menu Option: 2
| 000 000 |
| 000 000 |
Menu Option: 3
1) matrix1 - matrix2
2) matrix2 - matrix1
Choose option: 1
| 000 000 |
| 000 000 |
Menu Option: 3
1) matrix1 - matrix2
2) matrix2 - matrix1
Choose option: 2
| 000 000 |
| 000 000 |
Menu Option: 4
1) matrix1 * matrix2
2) matrix2 * matrix1
Choose option: 1
| 000 000 |
| 000 000 |
Menu Option: 4
1) matrix1 * matrix2
2) matrix2 * matrix1
Choose option: 2
| 000 000 |
| 000 000 |
Menu Option: 5
1) Transpose of matrix1
2) Transpose of matrix2
Choose option: 1
| 000 000 |
| 000 000 |
Menu Option: 5
1) Transpose of matrix1
2) Transpose of matrix2
Choose option: 2
| 000 000 |
| 000 000 |
Menu Option: 6
1) Saddle point of matrix1
2) Saddle point of matrix2
Choose option: 1
Saddle point is 0
Menu Option: 6
1) Saddle point of matrix1
2) Saddle point of matrix2
Choose option: 2
Saddle point is 0
Menu Option: -1

---------------------------
Test case 5 - All -ve elements
---------------------------

Chose a option from menu:
1) Input Matrix
2) Add Matrix
3) Subtract Matrix
4) Multiply matrix
5) Transpose of matrix
6) Saddle point of matrix (PRACTICE PROBLEM)
Menu Option: 1
Number of row in 1st matrix: 2
Number of columns in 1st matrix: 2
Number of row in 2nd matrix: 2
Number of columns in 2nd matrix: 2
----Input For Matrix 1----
Value of 0,0: -1
Value of 0,1: -7 
Value of 1,0: -5
Value of 1,1: -4
----Input For Matrix 2----
Value of 0,0: -4
Value of 0,1: -3
Value of 1,0: -7
Value of 1,1: -6
Menu Option: 2
| -05 -10 |
| -12 -10 |
Menu Option: 3
1) matrix1 - matrix2
2) matrix2 - matrix1
Choose option: 1
| 003 -04 |
| 002 002 |
Menu Option: 3
1) matrix1 - matrix2
2) matrix2 - matrix1
Choose option: 2
| -03 004 |
| -02 -02 |
Menu Option: 4
1) matrix1 * matrix2
2) matrix2 * matrix1
Choose option: 1
| 053 045 |
| 048 039 |
Menu Option: 4
1) matrix1 * matrix2
2) matrix2 * matrix1
Choose option: 2
| 019 040 |
| 037 073 |
Menu Option: 5
1) Transpose of matrix1
2) Transpose of matrix2
Choose option: 1
| -01 -05 |
| -07 -04 |
Menu Option: 5
1) Transpose of matrix1
2) Transpose of matrix2
Choose option: 2
| -04 -07 |
| -03 -06 |
Menu Option: 6
1) Saddle point of matrix1
2) Saddle point of matrix2
Choose option: 1
There is no saddle point
Menu Option: 6
1) Saddle point of matrix1
2) Saddle point of matrix2
Choose option: 2
Saddle point is -4
Menu Option: -1

---------------------------
Test Case 6 - Unit Matrix
---------------------------

Chose a option from menu:
1) Input Matrix
2) Add Matrix
3) Subtract Matrix
4) Multiply matrix
5) Transpose of matrix
6) Saddle point of matrix (PRACTICE PROBLEM)
Menu Option: 1
Number of row in 1st matrix: 2
Number of columns in 1st matrix: 2
Number of row in 2nd matrix: 3
Number of columns in 2nd matrix: 3
----Input For Matrix 1----
Value of 0,0: 1
Value of 0,1: 0
Value of 1,0: 0
Value of 1,1: 1
----Input For Matrix 2----
Value of 0,0: 1
Value of 0,1: 0
Value of 0,2: 0
Value of 1,0: 0
Value of 1,1: 1
Value of 1,2: 0
Value of 2,0: 0
Value of 2,1: 0
Value of 2,2: 1
Menu Option: 2
Matrix1 and Matrix2 have different number of rows and columns hence can't be added
Argument is not a matrix!
Menu Option: 3
1) matrix1 - matrix2
2) matrix2 - matrix1
Choose option: 1
Matrix1 and Matrix2 have different number of rows and columns hence can't be subtracted
Argument is not a matrix!
Menu Option: 3
1) matrix1 - matrix2
2) matrix2 - matrix1
Choose option: 2
Matrix1 and Matrix2 have different number of rows and columns hence can't be subtracted
Argument is not a matrix!
Menu Option: 4
1) matrix1 * matrix2
2) matrix2 * matrix1
Choose option: 1
Matrix can't be multiplied
Argument is not a matrix!
Menu Option: 4
1) matrix1 * matrix2
2) matrix2 * matrix1
Choose option: 2
Matrix can't be multiplied
Argument is not a matrix!
Menu Option: 5
1) Transpose of matrix1
2) Transpose of matrix2
Choose option: 1
| 001 000 |
| 000 001 |
Menu Option: 5
1) Transpose of matrix1
2) Transpose of matrix2
Choose option: 2
| 001 000 000 |
| 000 001 000 |
| 000 000 001 |
Menu Option: 6
1) Saddle point of matrix1
2) Saddle point of matrix2
Choose option: 1
There is no saddle point
Menu Option: 6
1) Saddle point of matrix1
2) Saddle point of matrix2
Choose option: 2
There is no saddle point
Menu Option: -1
'''
