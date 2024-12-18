## What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
import numpy as np
f = open('grid.txt', 'r')

table = np.array([[int(ch) for ch in line.split()] for line in f.readlines()])

product = 0

for row in range(table.shape[0]):
    for column in range(table.shape[1]):
        print(row, column)

        if column + 3 < 20:
            temp_product = table[row, column] * table[row, column + 1] * table[row, column + 2] * table[row, column + 3]
            if temp_product > product:
                product = temp_product
        
        if row + 3 < 20:
            temp_product = table[row, column] * table[row + 1, column] * table[row + 2, column] * table[row + 3, column]
            if temp_product > product:
                product = temp_product
        
        if column + 3 < 20 and row + 3 < 20:
            temp_product = table[row, column] * table[row + 1, column + 1] * table[row + 2, column + 2] * table[row + 3, column + 3]
            if temp_product > product:
                product = temp_product

        if column - 3 < 20 and row + 3 < 20:
            temp_product = table[row, column] * table[row + 1, column - 1] * table[row + 2, column - 2] * table[row + 3, column - 3]
            if temp_product > product:
                product = temp_product
print(product)