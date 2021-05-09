# Write a Python program to compute following computation on matrix:
# a) Addition of two matrices B) Subtraction of two matrices
# c) Multiplication of two matrices d) Transpose of a matrix

# take Matrix input
#  Additoin (M1, M2)
# Subtraction (M1, M2)
# Multiplication (M1, M2)
# Transpose(M1)

import numpy as np

import numpy.matlib


print("Please choose the operation you want to perform")
print("1. Additon Of Matrices")
print("2. Subtraction of Two Matrices")
print("3. Multiplication Of Two Matrices")
print("4. Transpose of a matrix")

M1 = [[1, 3, 4],
      [4, 5, 6],
      [6, 7, 8]]
M2 = [[1, 3],
      [4, 5],
      [6, 7]]


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


# Utility Function
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

    # print(addMatrices(M1, M2))
    # subtraction = subMatrices(M1, M2)
    # print(subtraction)


print(np.dot(M1, M2))
# print(np.add(M1, M2))


multi = multiplyMatrices(M1, M2)
multiKnown = np.dot(M1, M2)

comparison = multi == multiKnown

equal_arrays = comparison.all()

print(equal_arrays)

if (equal_arrays):
    print("SUCCESS")
print(multi)
