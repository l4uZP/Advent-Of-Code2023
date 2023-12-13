import trebuchet_numbers

class Number:
    def __init__(self, letters, digit):
        self.letters = letters
        self.digit = digit

numbers = [
    Number("one",1),
    Number("two",2),
    Number("three",3),
    Number("four", 4),
    Number("five",5),
    Number("six",6),
    Number("seven",7),
    Number("eight",8),
    Number("nine",9)
]

def transformLettersInNumbers(code):
    for number in numbers:
        code = code.replace(number.letters, str(number.digit))
    return code


def createNewArray(codes):
    newArray = []
    for code in codes:
        newCode = transformLettersInNumbers(code)
        newArray.append(newCode)
    return newArray


def getAllNumbers(codes):
    numericCodes = createNewArray(codes)
    return trebuchet_numbers.getAllNumbers(numericCodes)

# def getTotal(codes):
#     numericCodes = createNewArray(codes)
#     subTotals = trebuchet_numbers.getAllNumbers(numericCodes)
#     total = 0 
#     for subtotal in subTotals:
#         total = total + subtotal
#     return total