"""
Math 560
Project 3
Fall 2021

Partner 1:
Partner 2:
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    ##### Your implementation goes here. #####
    ans = []
    for u in adjList:
        u.dist = math.inf
        u.prev = None
    adjList[0].dist = 0
    for i in range(0,len(adjMat[0])-1):
        for u in adjList:
            for v in u.neigh:
                if v.dist > u.dist + adjMat[u.rank][v.rank] + tol:
                    v.dist = u.dist + adjMat[u.rank][v.rank]
                    v.prev = u
    for u in adjList:
        for v in u.neigh:
            if v.dist > u.dist + adjMat[u.rank][v.rank] + tol:
                temp = v
                v.prev = u
                ans.insert(0,temp.rank)
                while temp.prev!=v:
                    temp = temp.prev
                    ans.insert(0,temp.rank)
                ans.insert(0,temp.prev.rank)
                return ans

    return ans
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # Currently this only returns a copy of the rates matrix.
    return [[-math.log(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
