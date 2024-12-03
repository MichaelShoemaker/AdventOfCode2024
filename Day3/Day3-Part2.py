import re

def find_dos_donts(f:str):
    #Get the start and end position of every do() and don't()
    dos = []
    donts = []
    
    find_dos = re.finditer(r"do\(\)",f)
    find_donts = re.finditer(r'don\'t()',f)
    for i in find_dos:
        dos.append(i.span())
    for i in find_donts:
        donts.append(i.span())
    return dos, donts

def combine_recs(dos:list, donts:list):
    #Make a tuple of every do and don't with the second place being the ending span value
    #And sorted by the ending span value
    ldos = []
    ldonts = []
    for i in dos:
        ldos.append(('do', i[1]))
    for i in donts:
        ldonts.append(('dont', i[1]))
    moves = ldos+ldonts

    return sorted(moves, key = lambda x: x[1])

def make_raw_moves(dos_donts:list, f:str):
    #Go through each record
    spans = []
    s = [0]
    for i, n in enumerate(dos_donts):
        #Skip if do is already populated. As to capture the whole span if sequential records are do, do do etc
        if n[0] == 'do' and len(s) == 0:
            s = [n[1]]
        if n[0] == 'dont' and len(s) > 0:
            s.append(n[1])
            spans.append(s)
            s = []
        elif n[0] == 'dont' and len(s) == 0:
            pass
        if i == len(dos_donts)-1 and len(s) > 0:
            spans.append([s[0],len(f)])

    siffter = []
    for span in spans:
        siffter.append(f[span[0]:span[1]])
        
    for_processing = []
    for rec in siffter:
        for_processing.append(re.findall(r'mul\(\d+,\d+\)',rec))

    return for_processing


def get_digits(for_processing:list):
    digits = []
    for fp in for_processing:
        for rec in fp:
            digits.append((int(rec.replace('mul(','').replace(')','').split(',')[0]),int(rec.replace('mul(','').replace(')','').split(',')[1])))
    return digits

def tabulate(digits:list) -> int:
    total = 0
    for digit in digits:
        total += digit[0] * digit[1]
    return total


if __name__ == '__main__':
    f = open('input.txt').read()
    dos, donts = find_dos_donts(f)
    dos_donts = combine_recs(dos, donts)
    raw_do_pieces = make_raw_moves(dos_donts,f)
    for_total = get_digits(raw_do_pieces)
    print(tabulate(for_total))