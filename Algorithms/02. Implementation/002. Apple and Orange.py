# https://www.hackerrank.com/challenges/apple-and-orange/problem


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    apple_count = 0
    orange_count = 0

    for i in range(len(apples)):
        # print(i, apples[i] + a)
        if (apples[i] + a) >= s and (apples[i] + a <= t):
            apple_count += 1
    print(apple_count)

    for i in range(len(oranges)):
        # print(i, oranges[i] + b)
        if (oranges[i] + b) >= s and (oranges[i] + b <= t):
            orange_count += 1
    print(orange_count)





s = 7
t = 10
a = 4
b = 12
# m = 3
# n = 3
apples = [2, 3, -4]
oranges = [3, -2 ,-4]

countApplesAndOranges(s, t, a, b, apples, oranges)