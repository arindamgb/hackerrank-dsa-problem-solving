# https://www.hackerrank.com/challenges/simple-array-sum/problem
def simpleArraySum(ar):
    # Write your code here
    sum = 0
    for item in ar:
        sum += item
    return sum


arr = [1, 2, 3]

print(simpleArraySum(arr))
