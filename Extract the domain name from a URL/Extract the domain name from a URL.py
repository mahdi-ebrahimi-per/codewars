
# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    
    # استاندارد کردن
    # https://url  -> url  # or www.url
    # http://url  -> url  # or www.url
    if 'http:' in url:
        url = url[7:]

    elif 'https:' in url:
        url = url[8:]


    # اش را پاک کند www. داشت قسمت www اگر اولش
    # url -> url.com
    # www.url -> url.com
    if 'www.' in url:
        url = url[4:]

    # url.com -> [url, com][0] = name
    return url.split(".")[0]


print(domain_name("https://youtube.com"))
print(domain_name("www.xakep.ru"))
print(domain_name("http://google.co.jp"))
print(domain_name("http://google.com"))
print(domain_name("https://www.youtube.com"))








