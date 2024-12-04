from collections import Counter

def main(lines):
    
    left_list = []
    right_list = []
    
    for line in lines:
        left_list.append(int(line.split()[0]))
        right_list.append(int(line.split()[1]))
        
        
    zipped = zip(sorted(left_list), sorted(right_list))
    abs_zipped = [abs(x - y) for x,y in zipped]
    # print(abs_zipped)
    print(sum(abs_zipped))
    

    frequency_dict = Counter(right_list)
    # print(frequency_dict)
    total = []
    for i in left_list:
        value = frequency_dict.get(i)
        if(value == None):
            value = 0
        total.append(value*i)

    print(sum(total))
    


if __name__ == "__main__":
    # start = time.time()
    # file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().split("\n")
    main(lines)
    # end = time.time()
    # print("Time:", end-start)