def make_grid(file):
    grid = []
    f = open(file).readlines()
    for line in f:
        line = line.replace('\n','')
        grid.append([x for x in line])
    return grid

def rotate_grid(grid):
    """
    The rotation code below was found from this Stack Overflow post
    https://stackoverflow.com/questions/34347043/how-can-i-rotate-this-list-of-lists-with-python
    """
    return [list(row) for row in zip(*reversed(grid))]
            

def find_xmases(grid):
    found = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            try:
                if grid[i][j] == 'X' and grid[i-1][j] == 'M' and grid[i-2][j] == 'A' and grid[i-3][j] == 'S':
                    found += 1
                elif grid[i][j] == 'X' and grid[i+1][j] == 'M' and grid[i+2][j] == 'A' and grid[i+3][j] == 'S':
                    found += 1
                elif grid[i][j] == 'X' and grid[i][j-1] == 'M' and grid[i][j-2] == 'A' and grid[i][j-3] == 'S':
                    found += 1
                elif grid[i][j] == 'X' and grid[i][j+1] == 'M' and grid[i][j+2] == 'A' and grid[i][j+3] == 'S':
                    found += 1
            except Exception as e:
                pass  
    return found

if __name__ == '__main__':
    xmases = 0 
    grid = make_grid('test.txt')
    xmases += find_xmases(grid)
    for i in grid:
        print(i)
    print('###')
    for i in range(3):   
        grid = rotate_grid(grid)
        xmases += find_xmases(grid)
        # for i in grid:
        #     print(i)
        # print('###')
    print(xmases)