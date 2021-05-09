# Code is complete...battle-testing is remaining
# Write a Python program to compute following computation on matrix:
# a) Addition of two matrices B) Subtraction of two matrices
# c) Multiplication of two matrices d) Transpose of a matrix

# take Matrix input
#  Additoin (M1, M2)
# Subtraction (M1, M2)
# Multiplication (M1, M2)
# Transpose(M1)


# M1 = [[1, 3, 4],
#       [4, 5, 6],
#       [6, 7, 8]]
# M2 = [[1, 3],
#       [4, 5],
#       [6, 7]]


def addMatrices(m1, m2):
    m1Dimensions = calculateDimensions(m1)
    m2Dimensions = calculateDimensions(m2)
    if (m1Dimensions and m2Dimensions and m1Dimensions != m2Dimensions):
        print("ERROR (Addition Of Matrices): Matrix Dimensions are not matching !!! Dimensions are - {m1dims}, {m2dims}".format(
            m1dims=m1Dimensions, m2dims=m2Dimensions))
        return

    resultMatrix = table = [
        [0 for c in range(m1Dimensions[1])] for r in range(m1Dimensions[0])]

    for rowNo in range(m2Dimensions[0]):
        for colNo in range(m1Dimensions[1]):
            # print(rowNo, colNo)
            resultMatrix[rowNo][colNo] = m1[rowNo][colNo] + m2[rowNo][colNo]

    return resultMatrix


def subMatrices(m1, m2):
    m1Dimensions = calculateDimensions(m1)
    m2Dimensions = calculateDimensions(m2)
    if (m1Dimensions and m2Dimensions and m1Dimensions != m2Dimensions):
        print("ERROR (Addition Of Matrices): Matrix Dimensions are not matching !!! Dimensions are - {m1dims}, {m2dims}".format(
            m1dims=m1Dimensions, m2dims=m2Dimensions))
        return

    resultMatrix = table = [
        [0 for c in range(m1Dimensions[1])] for r in range(m1Dimensions[0])]

    for rowNo in range(m2Dimensions[0]):
        for colNo in range(m1Dimensions[1]):
            # print(rowNo, colNo)
            resultMatrix[rowNo][colNo] = m1[rowNo][colNo] - m2[rowNo][colNo]
    return resultMatrix


def multiplyMatrices(m1, m2):
    m1Dimensions = calculateDimensions(m1)
    m2Dimensions = calculateDimensions(m2)

    if(m1Dimensions[1] != m2Dimensions[0]):
        print('ERROR: No. of Cols and No. of rows not matching')
        return
    product = []
    for rowNo in range(m1Dimensions[0]):
        productRow = []
        for colNo in range(m2Dimensions[1]):
            sum = 0
            for itemNo in range(m1Dimensions[0]):
                # print(m1[rowNo][itemNo], m2[itemNo][colNo])
                sum += m1[rowNo][itemNo] * m2[itemNo][colNo]
            # print(sum)
            productRow.append(sum)
        product.append(productRow)
    return product


def transposeMatrix(m):
    dims = calculateDimensions(m)
    transpose = []
    for i in range(dims[1]):
        oneRow = []
        for j in range(dims[0]):
            oneRow.append(m[j][i])
        transpose.append(oneRow)
    return transpose


# Utility Functions
def calculateDimensions(m):
    rows = len(m)
    cols = 0
    # rowLens = []
    rowLen = len(m[1])
    for colNo in range(len(m)):
        if len(m[colNo]) != rowLen:
            print(
                "ERROR: Invalid Matrix - {}".format(m))
            return
    cols = rowLen
    return rows, cols


def takeMatrixInput():
    print("Taking Matrix Input...")
    rows = int(input("Please Enter No. of Rows : "))
    cols = int(input("Please Enter No. of Columns : "))
    m = []
    for i in range(rows):
        oneRow = []
        for j in range(cols):
            ele = int(input("Please enter element at ({}, {}) : ".format(i, j)))
            oneRow.append(ele)
        m.append(oneRow)
    return m


def printMatrix(m):
    if(m):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in m]))


firstTime = 1
print("Please choose the operation you want to perform")
print("1. Addition Of Matrices")
print("2. Subtraction of Two Matrices")
print("3. Multiplication Of Two Matrices")
print("4. Transpose of a matrix")
choice = 0
takeInputs = 1
# firstTime =
while (choice != -1):
    if(takeInputs):
        print('Please Enter both Matrices you want to perform operations on - ')
        print('Taking 1st matrix as input...')
        M1 = takeMatrixInput()
        print('Taking 2nd matrix as input...')
        M2 = takeMatrixInput()
        print('Matrix inputs taken successfully !!!')
        takeInputs = 0
        # firstTime = 1

    if (firstTime):
        print("Please choose the operation you want to perform")
        print("1. Addition Of Matrices")
        print("2. Subtraction of Two Matrices")
        print("3. Multiplication Of Two Matrices")
        print("4. Transpose of a matrix")
        print("5. Delete Previous Inputs and Take new Inputs")
        print("-1 to exit")
    choice = int(input("Please Enter Your Choice : "))

    if(choice == 1):
        print("The Addition Of Matrices is - ")
        printMatrix(addMatrices(M1, M2))

    elif(choice == 2):
        print("Choose one of the following")
        print("1. Substract Matrix 1 from 2")
        print("2. Substract Matrix 2 from 1")

        choice2 = int(input("Enter Your Choice : "))

        if(choice2 == 1):
            print("The Subtraction of Matrices is - ")
            printMatrix(subMatrices(M1, M2))

        elif(choice2 == 2):
            print("The Subtraction of Matrices is - ")
            printMatrix(subMatrices(M2, M1))

    elif(choice == 3):
        print('The Multiplication of Matrices is - ')
        printMatrix(multiplyMatrices(M1, M2))

    elif(choice == 4):
        print("Choose one of the following")
        print("1. Transpose Of Matrix 1")
        print("2. Transpose of Matrix 2")

        choice2 = int(input("Enter Your Choice : "))

        if(choice2 == 1):
            print("The Transpose of Matrix is - ")
            printMatrix(transposeMatrix(M1))

        elif(choice2 == 2):
            print("The Transpose of Matrix is - ")
            printMatrix(transposeMatrix(M2))

    elif(choice == 5):
        takeInputs = 1

    elif(choice == -1):
        break

# ==========================================================================================================================
# import numpy as np

# import numpy.matlib

# print(np.dot(M1, M2))
# print(np.add(M1, M2))
# multi = multiplyMatrices(M1, M2)
# multiKnown = np.dot(M1, M2)
# comparison = multi == multiKnown
# equal_arrays = comparison.all()
# print(equal_arrays)
# if (equal_arrays):
#     print("SUCCESS")
# print(multi)
