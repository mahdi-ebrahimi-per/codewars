
# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(words):
    return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))



print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))