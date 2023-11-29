# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


def breakingRecords(scores):
    # Write your code here
    max = scores[0]
    min = scores[0]

    maxCount = 0
    minCount = 0

    for score in scores:
        if score < min:
            minCount += 1
            min = score
        elif score > max:
            maxCount += 1
            max = score

    #print(maxCount, minCount)
    return[maxCount, minCount]



# scores = [12, 24, 10, 24]
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
result = breakingRecords(scores)

print(result)