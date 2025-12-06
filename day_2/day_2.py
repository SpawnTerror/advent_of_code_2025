#!/usr/bin/python3

def day_1_part_1():
    with open('day_2/sample.txt', 'r') as f:
        data = [line.strip().split(',') for line in f]

    print(data)

if __name__ == '__main__':
    day_1_part_1()