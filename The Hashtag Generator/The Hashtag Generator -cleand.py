# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output

#______

def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output

#_____

def generate_hashtag(s): return '#' +s.strip().title().replace(' ','') if 0<len(s)<=140 else False



print(generate_hashtag("codewars is nice"))  # → CodewarsIsNice










