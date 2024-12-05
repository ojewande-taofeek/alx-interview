#!/usr/bin/python3
"""
    Function that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
        As stated above
    """
    perimeter = 0
    for index in range(len(grid)):
        for inner_index in range(len(grid[index])):
            if grid[index][inner_index] == 1:
                perimeter += 4
                if index > 0 and grid[index-1][inner_index] == 1:
                    perimeter -= 2
                if inner_index > 0 and grid[index][inner_index-1] == 1:
                    perimeter -= 2
    return perimeter
