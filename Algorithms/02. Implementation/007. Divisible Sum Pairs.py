# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(0, n + 1):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                # print(ar[i], ar[j])
                count += 1
    return count



n = 6
k = 5
ar = [1, 2, 3, 4, 5, 6]

# n = 6
# k = 3
# ar = [1, 3, 2, 6, 1, 2]


pair = divisibleSumPairs(n, k, ar)
print(pair)