import os
import time

grid_width = 9
grid_height = 9

def ggn(num):
    if num == -1:
        return ' '
    return str(num)

def print_grid(grid = None):
    if not grid:
        return
    print('     1   2   3   4   5   6   7   8   9')
    print('   +---+---+---+---+---+---+---+---+---+')

    for i in range(len(grid)):
        print(f' {i+1} | {ggn(grid[i][0])}   {ggn(grid[i][1])}   {ggn(grid[i][2])} | {ggn(grid[i][3])}   {ggn(grid[i][4])}   {ggn(grid[i][5])} | {ggn(grid[i][6])}   {ggn(grid[i][7])}   {ggn(grid[i][8])} |')
        if i % 3 == 2:
            print('   +---+---+---+---+---+---+---+---+---+')
        else:
            print('   +   +   +   +   +   +   +   +   +   +')

def next_empty_cell(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == -1:
                return i, j
    return None, None

def solve_puzzle(grid):
    row, col = next_empty_cell(grid)
    
    if row == None:
        return grid

    for i in range(1, 10):
        grid[row][col] = i
        if check_grid(grid):
            if solve_puzzle(grid):
                return grid
        grid[row][col] = -1
    return False

def check_grid(grid):
    # check if rows have same length
    for row in grid:
        if len(row) != grid_width:
            return False

    # horizontal check
    for i in range(len(grid)):
        nums = []
        for j in range(len(grid[i])):
            if grid[i][j] != -1:
                if grid[i][j] in nums:
                    return False
                nums.append(grid[i][j])

    # vertical check
    for i in range(grid_width):
        nums = []
        for j in range(len(grid)):
            if grid[j][i] != -1:
                if grid[j][i] in nums:
                    return False
                nums.append(grid[j][i])
    
    # check if 3x3 squares are vaild
    for i in range(grid_width):
        if i % 3 == 0:
            for j in range(grid_width):
                if j % 3 == 0:
                    nums = []
                    for k in range(3):
                        for l in range(3):
                            if grid[i+k][j+l] != -1:
                                if grid[i+k][j+l] in nums:
                                    return False
                                nums.append(grid[i+k][j+l])
    return True 

def insert_grid():
    grid = [[-1 for j in range(grid_width)] for i in range(grid_height)]

    while True:
        os.system("cls")
        print_grid(grid)
        print('What do your want to do?')
        print('1. Insert a number')
        print(' - Enter the row and column number and the number in this format: x:y=n\n - Example: Row: 2 Column: 3 Value 4  looks like 3:2=4\n - if the field is empty use -1 as value')
        print('2. Solve the puzzle')
        print(' - Enter \'solve\'')
        print('3. Exit')
        print(' - Enter \'exit\'')
        
        choice = input('Enter your choice: ')
        if choice == 'exit':
            exit(1)
        elif choice == 'solve':
            return grid
        else:
            if len(choice) == 5 or len(choice) == 6:
                col = int(choice[0])
                row = int(choice[2])
                if len(choice) == 6:
                    val = int(choice[4]+choice[5])
                else:
                        val = int(choice[4])
                if row > grid_height or col > grid_width or row < 1 or col < 1:
                    print('Invalid row or column number')
                    continue
                if val > 9 or val < -1:
                    print('Invalid value')
                    continue
                grid[row-1][col-1] = val
                if (check_grid(grid)):
                    continue
                else:
                    grid[row-1][col-1] = -1

if __name__ == '__main__':
    input_grid = insert_grid()
    os.system('cls')
    start_time = time.time()
    print_grid(solve_puzzle(input_grid))
    print(f'Solved in {round(time.time() - start_time, 2)} seconds')
