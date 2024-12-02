def check_recs(reports:list):

    for report in reports:
        # print(report)
        # print(len(report))
        flag = ''
        for i, n in enumerate(report):
            #Skip the first record
            if i == 0:
                continue
            #Set the increase or decrease flag
            if report[i] > report[i-1]:
                flag = 'i'
            elif report[i] < report[i-1]:
                flag = 'd'
            
            #If there is a step bigger than 3 move on to the next report
            if abs(report[i] - report[i-1]) > 3 or abs(report[i] - report[i-1]) == 0:
                break
            if i < len(report) - 1:
                if flag == 'i' and report[i] > report[i+1]:
                    break
                if flag == 'd' and report[i] < report[i+1]:
                    break
            
            #If you get to the end 
            if i == len(report) - 1:
                if flag == 'd' and report[i] < report[i-1]:
                    return 'safe'
                if flag == 'i' and report[i] > report[i-1]:
                    return 'safe'
    return 'unsafe'


def make_possibilities(report:list):
    #For any given list, make every possible list excluding one of the values
    permetations = []
    for i in range(len(report)):
        permetations.append(report[:i]+report[i+1:])   
    #Include the original list
    permetations.append(report)
    return permetations


def make_reports(file):
    #Turn the lines of the input file into lists
    reports = []
    f = open(file).readlines()
    l = [x.replace('\n',' ') for x in f]
    for report in l:
        reports.append([int(x) for x in report.split(' ') if len(x)>0])
    return reports

if __name__ == '__main__':
    count = 0
    # x = make_possibilities([49, 47, 46, 43, 41, 38, 35, 57])
    # print(len(x))
    # print(check_recs(x))
    with open('bad_reports1.txt','w') as outfile:
        for report in make_reports('input.txt'):
            if check_recs(make_possibilities(report)) == 'safe':
                count += 1
            else:
                outfile.writelines(str(report)+'\n')
       bad