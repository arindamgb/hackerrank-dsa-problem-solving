# https://www.hackerrank.com/challenges/picking-numbers/problem

def pickingNumbers(a):
    # Write your code here
    subArr = []
    arr = []
    # a.sort()
    for i in range(len(a)):
        # print(a[i])
        subArr.append(a[i])
        for j in range(i + 1, len(a)):
            if abs(a[i] - a[j]) <= 1:
                for k in range(len(subArr)):
                    if abs(subArr[k] - a[j]) > 1:
                        break
                    elif k == len(subArr) - 1:
                        subArr.append(a[j])

        # arr.append(subArr)
        # subArr.clear()
        # print(subArr)
        arr.append(subArr)
        subArr = []

    # print(arr)
    max_len = 0
    for item in arr:
        if len(item) > max_len:
            max_len = len(item)

    return max_len

# a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
a = [1, 2, 2, 3, 1, 2]
print(pickingNumbers(a))