# codewars.com/kata/515decfd9dcfc23bb6000006/train/python

def is_valid_IP(strng):

    ip = strng.split('.')


    # is empty
    
    if strng == "":
        return False 

    # is a number → (0-9)
    for part in ip:
        if not part.isdigit():
            return False

    # not started with 0
    for part in ip:
        if len(part) > 1 and part[0] == "0":
            return False
    
    # 0-255
    for part in ip:
        if int(part) > 255:
            return False


    # check exist 4 part with max len 3 
    for part in ip:
        if len(part) <= 3 and len(ip) == 4 :
            return True

        else:
            return False



print(is_valid_IP('192.168.200')) #False
print(is_valid_IP('192.168.200.300')) #False
print(is_valid_IP('abc.def.ghi.jkl')) #False 
print(is_valid_IP('')) #False


