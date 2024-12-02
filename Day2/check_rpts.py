good = set()
bad = set()
with open('bad_reports.txt','r') as infile1:
    for line in infile1:
        good.add(line)

with open('bad_reports1.txt','r') as infile2:
    for line in infile2:
        bad.add(line)


diff = good-bad
with open('realdiff','w') as outfile:
    for i in diff:
        outfile.writelines(i+'\n')