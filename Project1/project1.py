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
    return listToSort

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
    print('DEFAULT measureTime')
    print()
    measureTime()