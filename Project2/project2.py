"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1:AS1134 Airu Song
Partner 2:SZ232 Sijie Zhou
Date:2021.11.3
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""

def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    # Clear the maze at the very beginning
    for v in maze.adjList:
        v.prev = None
        v.dist = math.inf
        v.visited = False

    ##### Your implementation goes here. #####
    if alg == 'DFS':
        #initialize a stack of size 10
        stack = Stack(10)
        #visit the start point
        stack.push(maze.start)
        maze.start.visited = True
        maze.start.dist = 0
        while not stack.isEmpty():
            v = stack.pop()
            dist = v.dist
            #get the exit of maze, return the outputs
            if v == maze.exit:
                maze.path = [None for x in range(0, v.dist+1)]
                maze.path[dist] = v.rank
                depth = v.dist
                #trace back by using the prev
                for i in range(0,depth):
                    prev = v.prev
                    v = prev
                    maze.path[depth - 1 - i] = v.rank
                maze.plot_maze_solution()
                return maze.path
            #if the vertex is not exit, visit it's neighbour one by one
            for n in v.neigh:
                if not n.visited:
                    n.visited = True
                    stack.push(n)
                    n.prev = v
                    n.dist = dist + 1

    if alg == 'BFS':
        queue = Queue()
        #visit the start vertex
        queue.push(maze.start)
        maze.start.dist = 0
        maze.start.visited=True
        while not queue.isEmpty():
             curr = queue.pop()
             dist = curr.dist
             #If visiting the exit vertex, return the results.
             if curr == maze.exit:
                maze.path = [None for x in range(0, curr.dist+1)]
                maze.path[dist] = curr.rank
                depth = curr.dist
                #trace back by using the prev
                for i in range(0,depth):
                    prev = curr.prev
                    curr = prev
                    maze.path[depth - 1 - i] = curr.rank
                maze.plot_maze_solution()
                return maze.path
             #if it's not the exit push the neighbour one by one
             for n in curr.neigh:
                 if not n.visited:
                    n.dist = curr.dist+1
                    n.prev = curr
                    n.visited = True
                    queue.push(n)

"""
Main function.
"""



if __name__ == "__main__":
    testMazes(False)

