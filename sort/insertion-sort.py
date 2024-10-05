# insertion sort 

def insertion_sort(myList):
    for i in range(1, len(myList)):
        temp = myList[i]
        j = i-1
        while temp < myList[j] and j > -1:
            myList[j+1] = myList[j]
            myList[j] = temp
            j -=1
    return myList


print(insertion_sort([13,12,4,5,2,65,32,5,3,0]))