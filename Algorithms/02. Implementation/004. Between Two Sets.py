# https://www.hackerrank.com/challenges/between-two-sets/problem


def getTotalX(a, b):
    # Write your code here

    # print(sum([all(i % x == 0 for x in a) and
    #            all(x % i == 0 for x in b) for i in range(max(a), min(b) + 1)]))

    result = []
    for i in range(max(a), min(b) + 1):
        factors_of_i_in_a = all(i % x == 0 for x in a)
        i_is_factor_of_all_in_b = all(x % i == 0 for x in b)

        if factors_of_i_in_a and i_is_factor_of_all_in_b:
            result.append(i)
    # print(result)
    return len(result)



# a = [2, 6]
#b = [24, 36]


a = [2, 4]
b = [16, 32, 96]


print(getTotalX(a,b))




