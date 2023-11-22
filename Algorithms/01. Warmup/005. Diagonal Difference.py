# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    # Write your code here
    ltr = 0
    rtl = 0

    n = len(arr)

    for i in range(0, n):
        ltr += arr[i][i]

    j = 0

    for i in range(n - 1, -1, -1):
        rtl += arr[i][j]
        j += 1

    diff = abs(ltr - rtl)

    return diff


arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

print(diagonalDifference(arr))