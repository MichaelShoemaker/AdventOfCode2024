import ast
from time import sleep
def make_data(file):
    keys = []
    orders = []
    f = open(file).readlines()
    for data in [x.replace('\n','') for x in f]:
        if '|' in data:
            keys.append(data)
        elif ',' in data:
            orders.append([int(x) for x in data.split(',')])
        else:
            print(f"No data in {data}")
    return keys, orders

def check_order(keys:list, orders:list) -> list:
    moves_to_check = []
    bad_lines = []
 


    for k in keys:
        #Put the page orders into a list of tuples as ints
        moves_to_check.append((int(k.split('|')[0]),int(k.split('|')[1])))
    # print(moves_to_check)
    for line in orders:
        # print(line)
        check_dict = {}
        for index, page in enumerate(line):
            check_dict[page] = index
        for move in moves_to_check:
            if move[0] in check_dict.keys() and move[1] in check_dict.keys():
                if check_dict[move[0]] > check_dict[move[1]]:
                    # print(f"Appending bad line {line} due to {move[0]} being after {move[1]}")
                    bad_lines.append(line)
                    break

    return set([str(order) for order in orders]) - set([str(line) for line in bad_lines]), bad_lines, moves_to_check

def create_master_order_list(moves):
   
    all_order = set()
    for i in moves:
        all_order.add(i[0])
        all_order.add(i[1])
    raw_all = list(all_order)

    while True:
        swapped = 'no'
        for move in moves:
            if raw_all.index(move[0]) > raw_all.index(move[1]):
                raw_all.pop(raw_all.index(move[0]))
                raw_all.insert(raw_all.index(move[1]), move[0])
                swapped = 'yes'
        if swapped == 'no':
            break
    return raw_all

def sort_bad_lists(order_key:list, bad_lines:list):
    fixed_lists = []
    for line in bad_lines:
        line = sorted(line, key=lambda x: order_key.index(x))
        fixed_lists.append(line)
    return fixed_lists


if __name__ == '__main__':
    keys, orders = make_data('test.txt')
    good_lines, bad_lines, moves_to_check = check_order(keys, orders)
    print(f"Sorting recs to make master key")
    master_sort_order = create_master_order_list(moves_to_check)
    print(f"Resorting bad lists")
    good_lists = sort_bad_lists(master_sort_order, bad_lines)
    # print(master_sort_order)
    total = 0
    #Part 1
    # for rec in good_lines:
    #     rec = ast.literal_eval(rec)
    #     total += rec[int(len(rec)/2-.5)]
    #     # print(rec[int(len(rec)/2-.5)])
    # print(total)

    # # Part 2
    for rec in good_lists:
        total += rec[int(len(rec)/2-.5)]
        # print(rec[int(len(rec)/2-.5)])
    print(total)
