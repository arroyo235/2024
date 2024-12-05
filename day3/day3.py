import re

def main(lines):

    line_values = []
    for line in lines:
        pattern = "mul\((\d{1,3}),(\d{1,3})\)"
        line_values.append(re.findall(pattern, line))
        
    result = 0
    for values in line_values:
        for value in values:
            result += multiply(value)
            
    print(result)
    
def multiply(numbers: tuple):
    return int(numbers[0]) * int(numbers[1])

    
if __name__ == "__main__":
    # start = time.time()
    file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)
    # end = time.time()
    # print("Time:", end-start)
