from time import sleep
def safe_unsafe(report:list):
    #Check all are increasing or decreasing
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
            # print(f"Value match {report}")
            return 'unsafe'
        elif direction == 'i' and report[i-1] > v:
            # print(f"Pattern Break {report}")
            return 'unsafe'
        elif direction == 'd' and report[i-1] < v:
            return 'unsafe'
        
        if abs(report[i-1] - v) > 3:
            return 'unsafe'
    # print(report)
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
    reports = make_reports('input.txt')
    for report in reports:
        result = safe_unsafe(report)
        if result == 'safe':
            count += 1
        else:
            pass
    print(count)