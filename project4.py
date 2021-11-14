"""
Math 560
Project 4
Fall 2021

Partner 1:
Partner 2:
Date:
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function
"""
def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')

    dist = 0 # This is a placeholder, remove and implement!
    edits = [] # This is a placeholder, remove and implement!

    # First, initialize the table.
    n = len(dest)
    m = len(src)
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    # Fill in the base cases (first row and first column).
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    # Fill in the table by iterating across each row.
    for i in range(1, m+1):
        for j in range(1,n+1):
            #If the two comparing symbols are the same,
            #there's no operation.
            if src[i-1] == dest[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1)
                dp[i][j]=min(dp[i][j],dp[i-1][j-1]+1)
    dist=dp[m][n]
    i=m
    j=n
    while i!=0 and j!=0:
        if src[i-1] == dest[j-1]:
            edits.append(('match',dest[j-1],j-1))
            i=i-1
            j=j-1
        else:
            if dp[i][j]-1==dp[i-1][j-1]:
                edits.append(('sub', str(dest[j-1]),i-1))
                i =i- 1
                j =j- 1
            elif dp[i][j]-1==dp[i-1][j]:
                edits.append(('delete', str(src[i-1]), i-1))
                i =i-1
            else:
                edits.append(('insert', str(dest[j-1]), i))
                j =j-1
    while i==0 and j>0:
        edits.append(('insert', str(dest[j-1]), i))
        j=j-1
    while j==0 and i>0:
        edits.append(('delete', str(src[i-1]), i-1))
        i=i-1


    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')
