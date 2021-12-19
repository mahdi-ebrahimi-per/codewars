# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

# حل نشده
# problem :  )( => True

def valid_parentheses(string):

    # 0 <= input length <= 100
    if len(string) > 100 or string=='':
        return False
    
    return True if string.count('(') == string.count(')') else False
