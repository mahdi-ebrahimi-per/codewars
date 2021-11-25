
# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    
    if 'http:' in url:
        url = url[7:]

    elif 'https:' in url:
        url = url[8:]

    elif 'www.' in url:
        url = url[4:]

    return url.split(".")[0]


print(domain_name("https://youtube.com"))
print(domain_name("www.xakep.ru"))
print(domain_name("http://google.co.jp"))
print(domain_name("http://google.com"))









