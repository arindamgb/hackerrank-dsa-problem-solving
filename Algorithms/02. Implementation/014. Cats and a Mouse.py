# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse(x, y, z):
    if abs(x - z) < abs(y - z):
        return 'Cat A'
    elif abs(x - z) > abs(y - z):
        return 'Cat B'
    elif abs(x - z) == abs(y - z):
        return 'Mouse C'


x = 1
y = 2
z = 3
print(catAndMouse(x, y ,z))