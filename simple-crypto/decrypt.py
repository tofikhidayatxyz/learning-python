import re
from constant import keycode

keypairs = [
    [2, -3],
    [-1, 2]
]

def parseFileToNuber(fileText) :
    fileText = fileText.replace('F', '0')
    return re.sub('\\D', "", fileText)

def getAlphabet(num) :
    return keycode[num - 1]

fileSource = './encrypted.txt'
fileDist = './decrypted.txt'

fileSourceData = open(fileSource, 'r').read()
fileToArray = [fileSourceData[i:i+4] for i in range(0, len(fileSourceData), 4)]
fileToNum = list(map(lambda x: parseFileToNuber(x), fileToArray))

mapedMatrix = [[], []]
if(len(list(fileToNum)) % 2 == 1) :
    fileToNum.append(len(keycode) - 1)

for key, value in enumerate(fileToNum) :
    if key < len(fileToNum) / 2 :
        mapedMatrix[0].append(int(value))
    else :
        mapedMatrix[1].append(int(value))

mapedParsedMatrix = [[], []]
# matrix to keypair
for key, value in enumerate(mapedMatrix[0]) :
    mapedParsedMatrix[0].append(value * keypairs[0][0])
    mapedParsedMatrix[1].append(value * keypairs[1][0])

for key, value in enumerate(mapedMatrix[1]) :
    mapedParsedMatrix[0][key] = mapedParsedMatrix[0][key] + (value *  keypairs[0][1])
    mapedParsedMatrix[1][key] = mapedParsedMatrix[1][key] + (value *  keypairs[1][1])

listingMatrix = mapedParsedMatrix[0] + mapedParsedMatrix[1]
finalArray = list(map(lambda x: getAlphabet(x), listingMatrix))
finalFile = ''.join(str(e) for e in finalArray)

fileResult = open(fileDist, 'w')
fileResult.write(finalFile)
fileResult.close()