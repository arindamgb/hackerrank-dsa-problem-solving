# https://www.hackerrank.com/challenges/compare-the-triplets/problem
def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    for i in range(0, 3):

        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1

    result = [int(alice), int(bob)]

    return result


a = [1, 2, 3]
b = [3, 2, 1]

print(compareTriplets(a, b))