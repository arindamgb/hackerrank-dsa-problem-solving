# https://hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    meet = False
    if x1 > x2 and v1 > v2:
        meet = False
    elif x1 < x2 and v1 < v2:
        meet = False
    else:
        for i in range(1, 10000):
            if (x1 + v1) == (x2 + v2):
                # print(f'Jump no {i}')
                meet = True
                break
            x1 += v1
            x2 += v2




    if meet == True:
        return 'YES'
    else:
        return 'NO'




#output = kangaroo(0, 2, 5, 3)   #NO
output = kangaroo(0, 3, 4, 2)  # YES
print(output)