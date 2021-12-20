# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

def generate_hashtag(s):
    
    # not empty and len not bigger that 140 
    if len(s) > 140 or len(s)==0:
        return False


    # split and stanradize : "code    wars" → ["code", "wars"]
    s = s.split(" ")
    space_count = s.count("")
    for i in range(space_count):
        s.remove('')


    # insert # in first
    s.insert(0, '#')
    

    # first letter of each capitalized
    index = 0
    for i in s:
        s[index] = i.capitalize()
        index += 1

    result = "".join(s)

    return result



print(generate_hashtag("codewars is nice"))  # → CodewarsIsNice










