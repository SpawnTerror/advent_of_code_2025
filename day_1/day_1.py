#!/usr/bin/python3

def day_1_part_1():

    '''
    Use modulo to get the reminder.
    '''

    with open('day_1/input.txt', 'r') as f:
       commands = [line.strip() for line in f]

    DIAL_SIZE = 100
    START_VALUE = 50
    TARGET_POS = 0
    passwords = 0
    
    current_pos = START_VALUE

    for command in commands:
        adjustment_value = int(command[1:])
        direction = command[0]
        if direction == "R":
            current_pos = (current_pos + adjustment_value) % DIAL_SIZE
        elif direction == "L":
            current_pos = (current_pos - adjustment_value) % DIAL_SIZE
        if current_pos == TARGET_POS:
            passwords = passwords + 1
    
    print(f'Total password part 1: {passwords}')

def day_1_part_2():

    '''
    Brute force the position one by one and count passwords up
    when it goes through zero position. Inefficient.
    '''

    with open('day_1/input.txt', 'r') as f:
        commands = [line.strip() for line in f]

    DIAL_SIZE = 100
    START_VALUE = 50
    TARGET_POS = 0
    passwords = 0

    current_pos = START_VALUE

    for command in commands:
        adjustment_value = int(command[1:])
        direction = command[0]   
        for _ in range(adjustment_value):
            if direction == 'L':
                current_pos = current_pos - 1
                if current_pos < 0:
                    current_pos = DIAL_SIZE - 1
            elif direction == 'R':
                current_pos = current_pos + 1
                if current_pos >= DIAL_SIZE:
                    current_pos = 0
            if current_pos == TARGET_POS:
                passwords = passwords + 1

    print(f'Total password part 2: {passwords}')

if __name__ == "__main__":

    day_1_part_1()
    day_1_part_2()
