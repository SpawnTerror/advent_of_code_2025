#!/usr/bin/python3
import re

def day_2_part_1():

    ranges = []
    invalid_ids_total = 0

    with open('day_2/input.txt', 'r') as f:
        for line in f:
            line = line.strip().split(',')
            for entry in line:
                if not entry:
                    continue
                range_start, range_end = entry.split('-')
                ranges.append([int(range_start), int(range_end)])

    for r in ranges:
        for number in range(r[0], r[1]+1):
            number_string = str(number)
            number_length = len(number_string)
            '''
            I assume I can cut the invalid ID in half and compare both parts
            '''
            split_value = number_length // 2
            part_1 = number_string[:split_value]
            part_2 = number_string[split_value:]
            if part_1 == part_2:
                invalid_ids_total = invalid_ids_total + number
        
    print(f'Part 1 invalid IDs total is {invalid_ids_total}.')

def day_2_part_2():

    ranges = []
    invalid_ids_total = 0

    with open('day_2/input.txt', 'r') as f:
        for line in f:
            line = line.strip().split(',')
            for entry in line:
                if not entry:
                    continue
                range_start, range_end = entry.split('-')
                ranges.append([int(range_start), int(range_end)])

    for r in ranges:
        for number in range(r[0], r[1] + 1):
            number_string = str(number)
            '''
            ^      : Start of the string
            (.+)   : Group 1. Match one or more characters (the pattern)
            \1+    : Match exactly what was found in Group 1, one or more times
            $      : End of the string
            '''
            if re.match(r'^(.+)\1+$', number_string):
                invalid_ids_total = invalid_ids_total + number

    print(f'Part 2 invalid IDs total is {invalid_ids_total}.')
            
if __name__ == '__main__':
    day_2_part_1()
    day_2_part_2()