import trebuchet_letters
import test_helpers

def test_transformLettersInNumbers_worksWithBasicExample():
    word = "two1nine"
    fn = trebuchet_letters.transformLettersInNumbers(word)
    test_helpers.AssertEquals(fn, "219")
test_transformLettersInNumbers_worksWithBasicExample()


def test_createNewArray_worksWithBasicExample():
    words = ["two1nine","ssss1nine6","pppppp","1100jjjjjj0"]
    fn = trebuchet_letters.transformLettersInNumbers(words)
    test_helpers.AssertEquals(fn, ["219","ssss196","pppppp","1100jjjjjj0"])
test_transformLettersInNumbers_worksWithBasicExample()

# def test_getTotal_worksWithBasicExample():
#     words = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]
#     fn = trebuchet_letters.getTotal(words)
#     test_helpers.AssertEquals(fn, 281)
# test_getTotal_worksWithBasicExample()

def test_getAllNumbers_worksWithBasicExample():
    words = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]
    fn = trebuchet_letters.getAllNumbers(words)
    print(fn)
    test_helpers.AssertEquals(fn, [29,83,13,24,42,14,76])
test_getAllNumbers_worksWithBasicExample()