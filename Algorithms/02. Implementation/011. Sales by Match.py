# https://www.hackerrank.com/challenges/sock-merchant/problem

def sockMerchant(n, ar):
    # Write your code here
    colors = dict()
    for item in ar:
        colors[item] = 0

    for sock in ar:
        colors[sock] += 1

    # print(colors)

    pairs = 0
    for sock in colors:
        colors[sock] = colors[sock] // 2
        pairs += colors[sock]

    return pairs



n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
print(sockMerchant(n, ar))