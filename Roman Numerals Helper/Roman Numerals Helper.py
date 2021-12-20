# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python

# not complited

class RomanNumerals:

    def __init__(self) -> None:
        self.roman_symbols = {
            'm' : 1000,
            'd' : 500,
            'c' : 100,
            'l' : 50,
            'x' : 10,
            'v' : 5,
            'i' : 1
        }

    def to_roman(self, val) -> str :

        inv_map = {v: k for k, v in self.roman_symbols.items()} # m:1000 → 1000:m
        result = ""
        for key, value in inv_map.items():  #key:1000|value:m
            while (int(val) - key) >= 0 :
                val -= key
                result += value
        
        return result.upper()
            
        

    def from_roman(self, roman_num):
        pass
        # roman_num = roman_num.lower()







instance = RomanNumerals()

print( instance.to_roman(4) ) #wrong
print( instance.to_roman(1776) ) # correct

# print( instance.from_roman('MDCCLXXVI') )








