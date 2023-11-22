# https://www.hackerrank.com/challenges/a-very-big-sum/problem

def aVeryBigSum(ar):
    # Write your code here
    sum = 0
    for item in ar:
        sum += item

    return sum


arr = [1, 2, 3, 4, 5]

print(aVeryBigSum(arr))