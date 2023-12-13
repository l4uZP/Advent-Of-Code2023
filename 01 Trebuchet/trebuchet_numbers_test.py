import trebuchet_numbers
import test_helpers

def test_findFirsNumberIn_worksWithBasicExample():
    word = "dhshdqq2344jkkjl11111o0"
    fn = trebuchet_numbers.findFirsNumberIn(word)
    test_helpers.AssertEquals(fn, "2")
test_findFirsNumberIn_worksWithBasicExample()

def test_findLastNumberIn_worksWithBasicExample():
    word = "dhshdqq2344jkkjl11111o0"
    fn = trebuchet_numbers.findLastNumberIn(word)
    test_helpers.AssertEquals(fn, "0")
test_findLastNumberIn_worksWithBasicExample()

def test_joinFirstAndLastNumber_worksWithBasicExample():
    word = "dhshdqq2344jkkjl11111o0"
    fn = trebuchet_numbers.joinFirstAndLastNumber(word)
    test_helpers.AssertEquals(fn, "20")
test_joinFirstAndLastNumber_worksWithBasicExample()

def test_getAllNumbers_worksWithBasicExample():
    wordsArray = ["dhshdqq2344jkkjl11111o0","1xxxxx8xxxxx0","xwe3xx1xxxxx8xxxxx01 ","ccccc0009x27hh"]
    sumArray = trebuchet_numbers.getAllNumbers(wordsArray)
    test_helpers.AssertEquals (sumArray, [20,10,31,7])
test_getAllNumbers_worksWithBasicExample()

def test_getTotal_worksWithBasicExample():
    wordsArray = ["dhshdqq2344jkkjl11111o0","1xxxxx8xxxxx0","xwe3xx1xxxxx8xxxxx01 ","ccccc0009x27hh"]
    total = trebuchet_numbers.getTotal(wordsArray)
    test_helpers.AssertEquals(total, 68)
test_getTotal_worksWithBasicExample()

def test_findFirstNumberIn_returnZeroWhenThereIsNoNumber():
    word = "aaaaaaaaaa"
    fn = trebuchet_numbers.findFirsNumberIn(word)
    test_helpers.AssertEquals(fn, 0)
test_findFirstNumberIn_returnZeroWhenThereIsNoNumber()

def test_findLastNumberIn_returnZeroWhenThereIsNoNumber():
    word = "aaaaaaaaaa"
    fn = trebuchet_numbers.findLastNumberIn(word)
    test_helpers.AssertEquals(fn, 0)
test_findLastNumberIn_returnZeroWhenThereIsNoNumber()

def test_findFirstNumberIn_returnZeroWhenEmptyStringIsGiven():
    word = ""
    fn = trebuchet_numbers.findFirsNumberIn(word)
    test_helpers.AssertEquals(fn, 0)
test_findFirstNumberIn_returnZeroWhenEmptyStringIsGiven()