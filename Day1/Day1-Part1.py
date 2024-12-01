def solve(file):
    #Define lists to hold numbers
    result = 0
    left = []
    right = []

    #Prep data from file and create lists
    f = open(file).readlines()
    y = [x.replace('\n','') for x in f]

    for s in y:
        nums = s.split('   ')
        left.append(int(nums[0]))
        right.append(int(nums[1]))


    #Sort the lists so they are in order
    left.sort()
    right.sort()

    #Calculate the result
    for i in range(0,len(left)):
        result += abs(left[i]-right[i])

    print(result)

if __name__ == '__main__':
    solve('input.txt')