#!/usr/bin/python3

def day_3_part_1():

    array_of_batteries = []
    total_joltage = 0

    with open('day_3/input.txt', 'r') as f:

        for line in f:
            line = line.strip()
            array_of_batteries.append(line)

    for entry in array_of_batteries:

        highest_number = 0  

        for i in range(len(entry) - 1):
            for j in range(i + 1, len(entry)):
                highest_number = max(highest_number,int(entry[i] + entry[j])
                )

        total_joltage += highest_number 

    print(f'Total joltage is {total_joltage}')

def day_3_part_2():

    pass

if __name__ == '__main__':
    day_3_part_1()
    day_3_part_2()