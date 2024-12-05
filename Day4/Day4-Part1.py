def make_grid(file):
    grid = []
    f = open(file).readlines()
    for line in f:
        line = line.replace('\n','')
        grid.append([x for x in line])
    return grid

# def rotate_grid(grid):
#     """
#     The rotation code below was found from this Stack Overflow post
#     https://stackoverflow.com/questions/34347043/how-can-i-rotate-this-list-of-lists-with-python
#     """
#     return [list(row) for row in zip(*reversed(grid))]
            

def find_xmases(grid):
    found = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
                if grid[i][j] == 'X':
                    #Used ChatGPT to trouble shoot boundary errors
                    #Backwards Vertical
                    if i >= 3 and grid[i-1][j] == 'M' and grid[i-2][j] == 'A' and grid[i-3][j] == 'S':
                        found += 1
                    #Forwards Vertical
                    if i + 3 < len(grid) and grid[i+1][j] == 'M' and grid[i+2][j] == 'A' and grid[i+3][j] == 'S':
                        found += 1
                    #Backwards Horizontal
                    if j >= 3 and grid[i][j-1] == 'M' and grid[i][j-2] == 'A' and grid[i][j-3] == 'S':
                        found += 1
                    #Forwards Horizontal
                    if j + 3 < len(grid[0]) and grid[i][j+1] == 'M' and grid[i][j+2] == 'A' and grid[i][j+3] == 'S':
                        found += 1
                    #Backwards Up and to the left
                    if i >= 3 and j >= 3 and grid[i-1][j-1] == 'M' and grid[i-2][j-2] == 'A' and grid[i-3][j-3] == 'S':
                        found += 1
                    #Forwards down and to the right
                    if i + 3 < len(grid) and j+3 < len(grid[0]) and grid[i+1][j+1] == 'M' and grid[i+2][j+2] == 'A' and grid[i+3][j+3] == 'S':
                        found += 1
                    #Forwards down and to the left
                    if i + 3 < len(grid) and j >= 3 and grid[i+1][j-1] == 'M' and grid[i+2][j-2] == 'A' and grid[i+3][j-3] == 'S':
                        found += 1
                    #Forwards up and to the right
                    if i >= 3 and j < len(grid[0])-3 and grid[i-1][j+1] == 'M' and grid[i-2][j+2] == 'A' and grid[i-3][j+3] == 'S':
                        found += 1
    return found

if __name__ == '__main__':
    xmases = 0 
    grid = make_grid('input.txt')
    xmases = find_xmases(grid)
    # for i in grid:
    #     print(i)
    # print('###')
    # for i in range(3):   
    #     grid = rotate_grid(grid)
    #     xmases += find_xmases(grid)
        # for i in grid:
        #     print(i)
        # print('###')
    print(xmases)