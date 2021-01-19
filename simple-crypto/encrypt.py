import random 
from constant import keycode, zeroKeyCode, keyRandom

keypairs = [
    [2, 3],
    [1, 2]
]

fileSource = './source.txt'
fileDist = './encrypted.txt'

def getkeyPairIndex(keyText) :
    keyToArray = list(keycode)
    for index, value in enumerate(keyToArray) :
        if(keyText == value) :
            return index + 1
    return keyText

def generateRandomKey(length) :
    keyResult = ""
    for i in range(length) :
        keyResult += keyRandom[random.randint(0,  len(keyRandom) - 1)]
    return keyResult

def generateSigKey(keyText) :
    resultText = keyText.replace('0', zeroKeyCode)
    if(len(resultText) < 4) :
        return f"{ generateRandomKey(4 - len(keyText)) }{ resultText }"
    else :
        return resultText 
    
#open file
fileSourceData = open(fileSource, 'r')
fileToArray = list(fileSourceData.read())
fileToNum = list(map(lambda x: getkeyPairIndex(x), fileToArray))

mapedMatrix = [[], []]

if(len(list(fileToNum)) % 2 == 1) :
    fileToNum.append(len(keycode) - 1)

for key, value in enumerate(fileToNum) :
    if key < len(fileToNum) / 2 :
        mapedMatrix[0].append(value)
    else :
        mapedMatrix[1].append(value)

mapedParsedMatrix = [[], []]
# matrix to keypair
for key, value in enumerate(mapedMatrix[0]) :
    mapedParsedMatrix[0].append(value * keypairs[0][0])
    mapedParsedMatrix[1].append(value * keypairs[1][0])

for key, value in enumerate(mapedMatrix[1]) :
    mapedParsedMatrix[0][key] = mapedParsedMatrix[0][key] + (value * keypairs[0][1])
    mapedParsedMatrix[1][key] = mapedParsedMatrix[1][key] + (value * keypairs[1][1])

listingMatrix = mapedParsedMatrix[0] + mapedParsedMatrix[1]
fileToKeyMap = map(lambda x: generateSigKey(str(getkeyPairIndex(x))), listingMatrix)
fileFinal = ''.join(str(e) for e in fileToKeyMap)

fileResult = open(fileDist, 'w')
fileResult.write(fileFinal)
fileResult.close()