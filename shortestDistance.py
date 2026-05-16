array = ["hello","World","There","Here"]
sizearr = len(array)
word = "There"

found = 0

def findis(array,start,sizearr,word):
    for i in range(sizearr):
        if word == array[i]:
            t = sizearr - i
            t2 = abs(sizearr - t)
            if t2 < t:
                return t2
            else :
                return t
    return -1



print(findis(array,2,sizearr,"hello"))