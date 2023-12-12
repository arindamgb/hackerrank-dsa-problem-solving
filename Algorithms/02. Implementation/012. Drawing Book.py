# https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    # Write your code here
    totalPage = n
    targetPage = p

    turnFromStart = 0
    currentPage = 1
    for page in range(1, totalPage + 1):
        if targetPage == currentPage:
            break
        if currentPage + 1 == targetPage or currentPage + 2 == targetPage:
            turnFromStart += 1
            break
        else:
            turnFromStart += 1
            currentPage += 2
    # print(turnFromStart)

    turnFromEnd = 0
    currentPage = totalPage
    for page in range(totalPage, 0, -1):
        if targetPage == currentPage:
            break
        if totalPage % 2 == 0:
            if currentPage - 1 == targetPage or currentPage - 2 == targetPage:
                turnFromEnd += 1
                break
            else:
                turnFromEnd += 1
                currentPage -= 2
        elif totalPage % 2 != 0:
            if currentPage - 1 == targetPage:
                break
            else:
                turnFromEnd += 1
                currentPage -= 2
    # print(turnFromEnd)

    if turnFromStart < turnFromEnd:
        return turnFromStart
    else:
        return turnFromEnd

n = 5
p = 3

print(pageCount(n, p))