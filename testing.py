from numpy import zeros
from numpy import array
from numpy import add


def addSimilarMatrices(a, b):
    """This adds two matrices of the same dimension"""
    for y in range(len(a)):
        for x in range(len(a[0])):
            a[y][x] = a[y][x] + b[y][x]
    return a


a = [[1,2,3],
     [3,2,1],
     [3,3,3],
     [41,4,2]]

b = [[1,4,3],
     [-6,2,1],
     [3,1,3],
     [41,4,2]]

# print(addSimilarMatrices(a, b))

aArray = array(a)
bArray = array(b)

cArray = add(aArray, bArray)


print(aArray)
print(bArray)

print(cArray)

q = zeros((4, 3))


listOfGuys = [a, b, q]



def addMatricesFromList(list):
    totalSum = zeros((len(list[0]), len(list[0][0])))
    # row = []
    # for i in range(len(list[0][0])):
    #     row.append(0)
    # for i in range(len(list[0])):
    #     sum.append(row)

    for matrix in list:
        totalSum = add(totalSum, matrix)

    return totalSum


print(addMatricesFromList(listOfGuys))
