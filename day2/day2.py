def main(lines):
    
    reports = []
    
    for line in lines:
        reports.append(line.split())
        
    reports = [[int(i) for i in report] for report in reports]

    safe = 0
    for report in reports:
        if (check_increasing(report)):
            safe += 1
        elif (check_decreasing(report)):
            safe += 1
            
    print(safe)

    # PART 2
    safe = 0
    for report in reports:
        if (check_increasing(report)):
            safe += 1
        elif (check_decreasing(report)):
            safe += 1
        elif (check_dampener(report)):
            safe += 1            
    
    print(safe)
        
def check_increasing(report):
    """
    Verifica si el reporte es creciente y cumple con las reglas.
    """
    for i in range(len(report)-1):
        x = report[i]
        y = report[i+1]
        if not(x < y and abs(x-y) >= 1 and abs(x-y) <= 3):
            return False

    return True
 
def check_decreasing(report):
    """
    Verifica si el reporte es decreciente y cumple con las reglas.
    """ 
    for i in range(len(report)-1):
        x = report[i]
        y = report[i+1]
        if not(x > y and abs(x-y) >= 1 and abs(x-y) <= 3):
            return False
    return True

# PART 2
def check_dampener(report:list):
    """
    Verifica si un reporte inseguro puede volverse seguro eliminando un nivel.
    """ 
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if check_increasing(modified_report) or check_decreasing(modified_report):
            return True
    return False

if __name__ == "__main__":
    # start = time.time()
    file = open("test.txt", "r")
    file = open("input.txt", "r") # 1203 too high, 605 too low, 623 too low, 627 bad, 634!
    lines = file.read().split("\n")
    main(lines)
    # end = time.time()
    # print("Time:", end-start)
