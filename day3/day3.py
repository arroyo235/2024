import re

def main(file):

    global do_pattern
    do_pattern = r"(?:^|do\(\))(.*?)(?:don't\(\)|$)"
    global mul_pattern
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    part1(file)
    part2(file)

def part1(file):
    line_values = []
    lines = file.split("\n")
    for line in lines:
        line_values.append(re.findall(mul_pattern, line))

    result = 0
    for values in line_values:
        for value in values:
            result += multiply(value)
            
    print(result)

def part2(file):
    line_values = []
    matches = re.findall(do_pattern, file, flags=re.DOTALL)
    
    for match in matches:
        line_values.append(re.findall(mul_pattern, match))
        
    result = 0
    for values in line_values:
        for value in values:
            result += multiply(value)
            
    print(result)

def multiply(numbers: tuple):
    return int(numbers[0]) * int(numbers[1])
    
if __name__ == "__main__":
    file = open("test.txt", "r")
    file = open("input.txt", "r")
    # lines = file.read().split("\n")
    main(file.read())
