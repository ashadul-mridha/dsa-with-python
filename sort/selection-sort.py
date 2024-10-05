# selection sort 
def selectionSort(myList):
    for i in range(len(myList) - 1):
        minIndex = i
        for j in range(i+1, len(myList)):
            if myList[j] < myList[minIndex]:
                minIndex = j
        if i != minIndex:
            temp = myList[minIndex]
            myList[minIndex] = myList[i]
            myList[i] = temp
    return myList

print(selectionSort([13,12,4,5,2,65,32,5,3,0]))