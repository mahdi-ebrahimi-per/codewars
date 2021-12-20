# Moving Zeros To The End

def move_zeros(array):

    # iter_arr = iter(array)
    result = []
    zeros = 0
    for item in array:

        if item != 0 :
            result.append(item)

        else:
            zeros += 1

    
    for i in range(zeros):
        result.append(0)

    return result



print(move_zeros([1,2,3,0,4,0,0,5,0,6]))