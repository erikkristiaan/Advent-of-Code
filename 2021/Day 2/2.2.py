#!/usr/bin/env python3

def main():

    horizontal_sum = 0
    vertical_sum = 0
    aim = 0

    with open("input.txt") as f:
        content = [i.split() for i in f.read().splitlines()]

    for i in content:
        if i[0] == 'forward':
            horizontal_sum += int(i[1])
            vertical_sum += int(i[1]) * aim
        elif i[0] == 'down':
            aim += int(i[1])
        elif i[0] == 'up':
            aim -= int(i[1])

    print(horizontal_sum * vertical_sum)

if __name__ == '__main__':
    main()