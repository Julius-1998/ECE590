"""
Math 560
Project 5
Fall 2020
Partner 1:
Partner 2:
Date:
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""
def prim(adjList, adjMat):
    #Start with anarbitrary vertex.
    # Initialize all costs to infinity and prev to null
    for v in adjList:
        v.prev = None
        v.cost = math.inf
        v.visited = False
    # Pick an arbitrary start vertex and set cost to 0,choose the start
    start = adjList[0]
    start.cost = 0

    pq = PriorityQueue(adjList)
    while not pq.isEmpty():
        v = pq.deleteMin()
        v.visited = True
        for neighbor in v.neigh:
            if not neighbor.visited:
                if neighbor.cost > adjMat[v.rank][neighbor.rank]:
                    neighbor.cost = adjMat[v.rank][neighbor.rank]
                    neighbor.prev = v

    return


################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):

    for v in adjList:
        makeset(v)
    X = []

    for e in edgeList:
        u, v = e.vertices
        if not find(u).isEqual(find(v)):
            X.append(e)
            union(u, v)

    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union
These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    v.pi = v
    v.height = 0

    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.
"""
def find(v):
    while not v.isEqual(v.pi):
        v = v.pi

    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    ru = find(u)
    rv = find(v)

    if ru.isEqual(rv):
        return

    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv

    else:
        ru.pi = rv

        rv.height += 1

    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):

    tour = []
    for v in adjList:
        v.visited = False

    st = []
    st.append(start)

    while len(st)!=0:
        curr = st.pop(-1)
        curr.visited = True
        tour.append(curr.rank)

        for neigh in curr.mstN:
            if neigh.visited == False:
                st.append(neigh)


    tour.append(adjList[0].rank)

    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))

