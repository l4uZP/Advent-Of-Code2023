import trebuchet_numbers
import trebuchet_letters

def getResultFrom(input):
    with open(input) as codes:
        return trebuchet_numbers.getTotal(codes)
    
def getResultFrom2(input):
    with open(input) as codes:
        return trebuchet_letters.getTotal(codes)

print("First: ",getResultFrom(input = "input.txt"))
print("Second: ",getResultFrom2(input = "input.txt"))