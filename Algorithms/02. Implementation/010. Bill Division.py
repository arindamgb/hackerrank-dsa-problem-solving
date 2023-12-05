# https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill, k, b):
    # Write your code here

    total_bill = 0
    for index, price in enumerate(bill):
        if index == k:
            continue
        total_bill += price

    #print(total_bill)

    if b > total_bill/2:
        print(int((b - total_bill/2)))
    else:
        print('Bon Appetit')



bill = [3, 10, 2, 9]
k = 1
b = 7

bonAppetit(bill, k, b)