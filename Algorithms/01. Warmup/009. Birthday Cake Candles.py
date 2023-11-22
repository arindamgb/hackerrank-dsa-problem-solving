# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(candles):
    # Write your code here
    count = candles.count(max(candles))
    return count

candles = [4, 4, 1, 3]

print(birthdayCakeCandles(candles))