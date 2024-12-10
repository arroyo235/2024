import re
import numpy as np

def main(lines):
    global page_ordering_rules
    page_ordering_rules = []
    updates = []
    for line in lines:
        if re.match(r"\d{2}\|\d{2}", line) != None:
            page_ordering_rules.append(line.split("|"))
            # page_ordering_rules.append(line)
        elif re.match(r"(?:\d{2},)*\d{2}", line) != None:
            updates.append(line.split(","))
        else:
            continue
           
    correct_updates = []
    for update in updates:
        # print(update)
        if eval_update(update):
            correct_updates.append(int(update[len(update) // 2]))
        # print()
        
    print(sum(correct_updates))
def eval_update(update:list):

    rules_found = 0
    for i in range(len(update)-1):
        x = update[i]
        y = update[i+1]
        if ([x,y] in page_ordering_rules):
            # print("Rule", [x,y],"found")
            rules_found += 1
            
    return True if (rules_found == len(update)-1) else False

    
if __name__ == "__main__":
    file = open("test.txt", "r")
    file = open("input.txt", "r")
    lines = file.read().splitlines()
    main(lines)
