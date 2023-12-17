# https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    budgetMatches = []
    for key in keyboards:
        for dri in drives:
            if key + dri <= b:
                budgetMatches.append(key + dri)

    if len(budgetMatches) == 0:
        return -1
    else:
        return max(budgetMatches)


keyboards = [40, 50, 60]
drives = [5, 8, 12]
b = 60

print(getMoneySpent(keyboards, drives, b))