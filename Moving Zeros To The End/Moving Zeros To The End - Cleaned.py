# Moving Zeros To The End


def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)


#___________

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))




print(move_zeros([1,2,3,0,4,0,0,5,0,6]))