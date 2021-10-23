"""
Math 560
Project 1
Fall 2021

Partner 1:
Partner 2:
Date:
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    for i in range(len(listToSort)):
        minIndex = i
        for j in range(i+1, len(listToSort)):
            if(listToSort[j] < listToSort[minIndex]):
                minIndex = j
            pass
        pass
        temp = listToSort[i]
        listToSort[i] = listToSort[minIndex]
        listToSort[minIndex] = temp
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    for i in range(len(listToSort)):
        num = listToSort[i]
        j = i-1
        while j >=0 and listToSort[j]>listToSort[j+1]:
            listToSort[j+1],listToSort[j] = listToSort[j],listToSort[j+1]
            j = j-1
        pass
        listToSort[j+1] = num
    pass

    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):
    if len(listToSort) <= 1:
        return
    else:
        m = len(listToSort)//2
        l = listToSort[:m]
        r = listToSort[m:]
        MergeSort(l)
        MergeSort(r)
        lPivot = 0
        rPivot = 0
        ansPivot = 0
        while lPivot < len(l) and rPivot < len(r):
            if l[lPivot] < r[rPivot]:
                listToSort[ansPivot] = l[lPivot]
                lPivot = lPivot + 1
            else:
                listToSort[ansPivot] = r[rPivot]
                rPivot = rPivot + 1
            ansPivot = ansPivot + 1
        while lPivot < len(l):
            listToSort[ansPivot] = l[lPivot]
            lPivot = lPivot + 1
            ansPivot = ansPivot + 1
        while rPivot < len(r):
            listToSort[ansPivot] = r[rPivot]
            rPivot = rPivot + 1
            ansPivot = ansPivot + 1
    return listToSort
"""

QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    if j-i<=1:
        return listToSort
    s = partition(listToSort,i,j)
    QuickSort(listToSort,i,s)
    QuickSort(listToSort,s+1,j)
    return listToSort

def partition(list,begin,end):
    pivot = begin
    list[pivot],list[end-1] = list[end-1],list[pivot]
    l = begin
    for i in range(begin,end-1):
        if list[i] < list[end-1]:
            list[l],list[i] = list[i],list[l]
            l = l+1
    list[l],list[end-1] = list[end-1],list[l]
    return l
"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)