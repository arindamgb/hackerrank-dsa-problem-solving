# https://www.hackerrank.com/challenges/counting-valleys/problem


def countingValleys(steps, path):
    # Write your code here

    valleyCount = 0
    level = 0
    for step in path:
        if level == 0 and step == 'D':
            valleyCount += 1
        # print(level)

        if step == 'D':
            level -= 1
        elif step == 'U':
            level += 1

    return valleyCount

# steps = 8
# path = 'UDDDUDUU'

steps = 12
path = 'DDUUDDUDUUUD'
print(countingValleys(steps, path))