# https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    # Write your code here
    arr.sort()

    min = 0
    max = 0

    for i in range(0, 4):
        min += arr[i]

    for i in range(1, 5):
        max += arr[i]

    print(f'{min} {max}')


arr = [1, 3, 5, 7, 9]

miniMaxSum(arr)