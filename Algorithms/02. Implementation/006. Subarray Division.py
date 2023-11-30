# https://www.hackerrank.com/challenges/the-birthday-bar/problem


def birthday(s, d, m):
    # Write your code here
    bars = s
    len_of_segment = m
    sum_of_integers = d

    count = 0
    for i, bar in enumerate(bars):
        if i > len(bars) - len_of_segment:
            #print(len(bars))
            #print(f'{i} - {bar}')
            #print('break')
            break
        #print(f'{i} - {bar}')
        sum = 0
        for y in range(i, i + len_of_segment):
            sum += bars[y]
        #print(sum)

        if sum == sum_of_integers:
            count += 1

    #print(count)
    return count





s = [2, 2, 1, 3, 2]
d = 4
m = 2

# s = [1, 2, 1, 3, 2]
# d = 3
# m = 2

# s = [1, 1, 1, 1, 1]
# d = 2
# m = 3

# s = [4]
# d = 4
# m = 1

result = birthday(s, d, m)
print(result)