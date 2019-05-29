"""
image compression
Name: Aaron Gould
"""


from imageTools import *
import time

from scipy.linalg import svd
from numpy import array
from numpy import diag
from numpy import nditer
from numpy import add
from numpy import dot
from numpy import zeros


def turnIntoMatrix(pic):
    """This turns any pic into a gray-scale matrix"""
    matrix = []
    width = pic.getWidth()
    height = pic.getHeight()
    for y in range(height):
        row = []
        for x in range(width):
            (r, g, b) = pic.getColor(x, y)
            row.append(((0.3 * r) + (0.59 * g) + (0.11 * b)))
        matrix.append(row)
    return matrix

def turnIntoPicture(matrix):
    """This turns any matrix (array of arrays) into an imageTools picture"""
    newPic = Picture(len(matrix[1]), len(matrix))

    for y in range(newPic.getHeight()):
        for x in range(newPic.getWidth()):
            newPic.setColor(x, y, (matrix[y][x] / 3, matrix[y][x] / 3, matrix[y][x] / 3))

    return newPic


def compress(U, s, VT, i):
    """This function takes the first svd to make a very basic compression"""
    spectrals = []
    for j in range(i):
        spectrals.append(multiply(s[j], U[:,j], VT[j,:]))

    compressed = []
    row = []
    for i in range(len(VT)):
        row.append(0)
    for i in range(len(U)):
        compressed.append(row)

    return addMatricesFromList(spectrals)
    # return compressed

def addMatricesFromList(list):
    totalSum = zeros((len(list[0]), len(list[0][0])))

    for matrix in list:
        totalSum = add(totalSum, matrix)

    return totalSum

def addSimilarMatrices(a, b):
    """This adds two matrices of the same dimension"""
    for y in range(len(a)):
        for x in range(len(a[0])):
            a[y][x] = a[y][x] + b[y][x]
    return a

def multiply(s, u, v):
    product = []

    for i in nditer(u):
        row = []
        for j in nditer(v):
            row.append(s*i*j)
        product.append(row)

    return product

# def compress(U, s, VT, spectrals):
#     """First creates a blank matrix then fills it up with spectral decompositions"""
#     matrixSum = []
#     row = []
#     for i in range(len(VT)):
#         row.append(0)
#     for i in range(len(U)):
#         matrixSum.append(row)
#
#     for i in range(spectrals):
#         y = 0
#         for rowElement in nditer(U[:,i]):
#             x = 0
#             for columnElement in nditer(VT[i,:]):
#                 matrixSum[y][x] += s[i] * rowElement * columnElement
#                 x += 1
#             y += 1
#
#     return matrixSum


if __name__ == "__main__":

    originalEiffel = Picture("minneapolis.jpg")
    eiffelMatrix = turnIntoMatrix(originalEiffel)
    eiffelPic = turnIntoPicture(eiffelMatrix)
    actualEiffelMatrix = array(eiffelMatrix)

    U, s, VT = svd(actualEiffelMatrix)

    time.sleep(.5)
    compressedMatrix = compress(U, s, VT, 25)
    compressedPhoto = turnIntoPicture(compressedMatrix)
    compressedPhoto.show()

    # betterCompressedMatrix = compress(U, s, VT, 3)
    # for row in betterCompressedMatrix:
    #     print(row)

    input("Done... hit key to end program...")

