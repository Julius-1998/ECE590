"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1:
Partner 2:
Date:
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

    ##### Your implementation goes here. #####
    if alg == 'DFS':
        stack = Stack(10)
        stack.push(maze.start)
        maze.start.visited = True
        maze.start.dist = 0
        while not stack.isEmpty():
            v = stack.pop()
            dist = v.dist
            if v == maze.exit:
                maze.path = [None for x in range(0, v.dist+1)]
                maze.path[dist] = v.rank
                depth = v.dist
                for i in range(0,depth):
                    prev = v.prev
                    v = prev
                    maze.path[depth - 1 - i] = v.rank
                maze.plot_maze_solution()
                return maze.path
            for n in v.neigh:
                if not n.visited:
                    n.visited = True
                    stack.push(n)
                    n.prev = v
                    n.dist = dist + 1

    return []
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
