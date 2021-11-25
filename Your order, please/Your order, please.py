
# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):

    # قسیم بندی جمله از طریق اسپیس بین کلمات
    sentence_splited = sentence.split(" ")

    nums = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

    words = {}

    # اعداد درون هر کلمه را چک میکند
    # میکند words کلمه را به عنوان کلید و عددش را به عنوان مقدار وارد دیکشنری 
    for part in sentence_splited:
        for num in nums:
            if str(num) in part:
                words[part] = num


    # کلمات را از دیکشنری به کمک عدد ولیو اش سورت میکند
    sorted_words = dict(sorted(words.items(), key=lambda item: item[1]))

    # فقط کلید های دیکشنری را بر میددارد و آن را در قالب متن میکند
    result_words = " ".join(list(sorted_words.keys()))

    return result_words




print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))


