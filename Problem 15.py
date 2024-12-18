import numpy as np # type: ignore

nodes = np.zeros([21, 21])

count = 0

def parse_grid(row, col):
    global count
    print(row, col, count)
    if row == 21 or col == 21:
        print('reached border')
        return 1
    count += parse_grid(row, col + 1)
    count += parse_grid(row + 1, col)
    return 1

parse_grid(0, 0)