# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zer = 0

    for item in arr:
        if item > 0:
            pos += 1
        elif item < 0:
            neg += 1
        elif item == 0:
            zer += 1

    numbs = len(arr)

    pos_r = pos / numbs
    neg_r = neg / numbs
    zer_r = zer / numbs

    print(f'{pos_r:6f}')
    print(f'{neg_r:6f}')
    print(f'{zer_r:6f}')


arr = [-4, 3, -9, 0, 4, 1]

plusMinus(arr)