#!/usr/bin/python3

def day_4_part_1():

    array_of_scrolls = []
    total_joltage = 0

    with open('day_4/sample.txt', 'r') as f:

        for line in f:
            line = line.strip()
            for location in line:
                array_of_scrolls.append(line)

    for entry in array_of_scrolls:
        print(entry)
        

def day_4_part_2():

    pass

if __name__ == '__main__':
    day_4_part_1()
    day_4_part_2()