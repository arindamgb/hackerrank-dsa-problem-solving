# https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    # Write your code here
    sp = n - 1
    ha = n - sp

    while sp > -1:

        for i in range(1, sp + 1):
            print(' ', end='')

        for j in range(1, ha + 1):
            print('#', end='')

        sp -= 1
        ha += 1

        print('')


n = 4
staircase(n)
