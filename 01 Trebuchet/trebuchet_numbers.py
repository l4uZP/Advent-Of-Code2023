def findFirsNumberIn(code):
    for character in code:
        if isNumber(character):
            return character
    return 0

def findLastNumberIn(code):
    for character in code [::-1]:
        if isNumber(character):
            return character
    return 0

def isNumber(character):
    return character == "0" or character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9"

def joinFirstAndLastNumber(code):
    return findFirsNumberIn(code) + findLastNumberIn(code)

def getAllNumbers(codes):
    results = []
    for code in codes:
        newNum = int(joinFirstAndLastNumber(code))
        results.append(newNum)
    return results

def getTotal(codes):
    subTotals = getAllNumbers(codes)
    total = 0 
    for subtotal in subTotals:
        total = total + subtotal
    return total