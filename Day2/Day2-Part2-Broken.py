from time import sleep
#After a bad level is found check if removing a level would result in a safe report
def check_again(report:list):
    if report[0] < report[1]:
        direction = 'i'
    elif report[0] > report[1]:
        direction = 'd'
    else:
        return 'unsafe'
    
    for i, v in enumerate(report):
        #Skip the first index
        if i - 1 < 0:
            continue
        #Check if it breaks the increase or decrease rule
        if report[i-1] == v:
            return 'unsafe'
        elif direction == 'i' and report[i-1] > v:
            return 'unsafe'
        elif direction == 'd' and report[i-1] < v:
            return 'unsafe'
        if abs(report[i-1] - v) > 3:
            return 'unsafe'
    return 'safe'

def safe_unsafe(report:list):
    strikes = 0
    #Check all are increasing or decreasing
    if report[0] < report[1]:
        direction = 'i'
    elif report[0] > report[1]:
        direction = 'd'
    else:
        if check_again(report[1:])=='safe' or check_again([report[0]]+report[2:]) =='safe':
            return 'safe'
        else:
            return 'unsafe'

    for i, v in enumerate(report):
        #Skip the first index
        if i - 1 < 0:
            continue
        #Check if it breaks the increase or decrease rule
        if report[i-1] == v:
            if check_again(report[:i]+report[i+1:])=='safe' or check_again(report[:i-1]+report[i:])=='safe'or check_again(report[1:]) or check_again(report[:-1])== 'safe':
                return 'safe'
            else:
                return 'unsafe'
        elif direction == 'i' and report[i-1] > v:
            if check_again(report[:i]+report[i+1:])=='safe' or check_again(report[:i-1]+report[i:]) =='safe'or check_again(report[1:]) or check_again(report[:-1])== 'safe':
                return 'safe'
            else:
                return 'unsafe'
        elif direction == 'd' and report[i-1] < v:
            if check_again(report[:i]+report[i+1:])=='safe' or check_again(report[:i-1]+report[i:]) =='safe' or check_again(report[1:]) == 'safe' or check_again(report[:-1])== 'safe':
                return 'safe'
            else:
                return 'unsafe'
        if abs(report[i-1] - v) > 3:
            if check_again(report[:i]+report[i+1:])=='safe' or check_again(report[:i-1]+report[i:]) =='safe' or check_again(report[1:]) == 'safe' or check_again(report[:-1])== 'safe':
                return 'safe'
            else:
                return 'unsafe'
    return 'safe'



def make_reports(file):
    reports = []
    f = open(file).readlines()
    l = [x.replace('\n',' ') for x in f]
    for report in l:
        reports.append([int(x) for x in report.split(' ') if len(x)>0])
    return reports

if __name__ == '__main__':
    count = 0
    reports = make_reports('test.txt')
    with open('bad_reports.txt','w') as outfile:

        for report in reports:
            result = safe_unsafe(report)
            if result == 'safe':
                count += 1
            else:
                outfile.writelines(str(report)+'\n')
    print(count)
    # 612 is too low