def get_good_recs(file):
    total = 0
    f = open(file).read()
    dirty_recs = f.split('mul')
    for i in dirty_recs:
        if '(' in i and '(' in i:
            inter = i.split(')')[0].split('(')
            try:
                non_nums = inter[1].split(',')
                if len(non_nums) == 2 and non_nums[0].isnumeric() and non_nums[1].isnumeric():
                    print('hit')
                    total += int(non_nums[0]) * int(non_nums[1])
            except Exception as e:
                pass
    print(total)


if __name__ == '__main__':
    get_good_recs('input.txt')