from main import *

def turnIntoRGBMatrices(image):
    rgb = [[],[],[]]

    for y in range(image.getHeight()):
        rRow = []
        gRow = []
        bRow = []
        for x in range(image.getWidth()):
            (r, g, b) = image.getColor(x, y)
            rRow.append(r)
            gRow.append(g)
            bRow.append(b)

        rgb[0].append(rRow)
        rgb[1].append(gRow)
        rgb[2].append(bRow)

    return rgb

def turnRGBMatricsToImage(matrices):
    newPic = Picture(len(matrices[0][1]), len(matrices[0]))
    for y in range(newPic.getHeight()):
        for x in range(newPic.getWidth()):
            newPic.setColor(x, y, (matrices[0][y][x], matrices[1][y][x], matrices[2][y][x]))

    return newPic



if __name__ == "__main__":
    originalEiffel = Picture("minneapolis.jpg")
    eiffelRGB = turnIntoRGBMatrices(originalEiffel)
    newEiffel = turnRGBMatricsToImage(eiffelRGB)
    newEiffel.show()

    rU, rs, rVT = svd(eiffelRGB[0])
    gU, gs, gVT = svd(eiffelRGB[1])
    bU, bs, bVT = svd(eiffelRGB[2])

    rCompressedMatrix = compress(rU, rs, rVT, 25)
    gCompressedMatrix = compress(gU, gs, gVT, 25)
    bCompressedMatrix = compress(bU, bs, bVT, 25)



    rgbCompressedPhoto = turnRGBMatricsToImage([rCompressedMatrix,gCompressedMatrix,bCompressedMatrix])
    rgbCompressedPhoto.show()

    time.sleep(.5)


    input("press any key to continue")
