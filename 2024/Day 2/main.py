def read_file(file_name):
    with open(file_name, 'r') as data:
        reports = []
        for line in data:
            report = line.split()
            report = [int(item) for item in report]
            reports.append(report)
    return reports

def first_task(reports):
    safe = len(reports)
    for report in reports:

        sorted_asc = report.copy()
        sorted_des = report.copy()

        sorted_asc.sort()
        sorted_des.sort(reverse = True)

        if report != sorted_asc and report != sorted_des:
            safe -= 1
            continue;
        for i in range(len(report) - 1):
            if (abs(report[i+1] - report[i]) > 3 or abs(report[i+1] - report[i]) < 1):
                safe -= 1
                break;
    print(safe)


def validate_report(report):
    sign = None
    for i in range(0, len(report) - 1):
        s = (report[i+1] - report[i]) > 0
        if sign is None:
            sign = s
        elif sign != s:
            return i
        if (abs(report[i+1] - report[i]) > 3 or abs(report[i+1] - report[i]) < 1):
            return i
    return -1

def second_task(reports):
    safe = len(reports)
    for report in reports:
        res = validate_report(report)
        if  res != -1:
            report_ = report.copy()
            report__ = report.copy()
            report.pop(res)
            report_.pop(res + 1)
            report__.pop(res - 1)
            if validate_report(report) != -1 and validate_report(report_) != -1 and validate_report(report__) != -1:
                safe -= 1
    print(safe)



if __name__ == '__main__':
    reports= read_file("Day 2/input.txt")
    first_task(reports)
    second_task(reports)
    