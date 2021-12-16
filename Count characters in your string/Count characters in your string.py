# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

def count(string):

    chars = set(string)

    charCount = list(map(lambda x:string.count(x), chars))

    return dict(zip(chars, charCount))


print(count("aaab"))