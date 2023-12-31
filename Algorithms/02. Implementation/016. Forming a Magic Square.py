# https://www.hackerrank.com/challenges/magic-square-forming/problem

def formingMagicSquare(s):
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    min_cost = float("inf")

    for m_sqr in magic_squares:
        current_cost = 0
        for rs, ms in zip(s, m_sqr):
            # cost = sum(abs(x - y) for x, y in zip(rs, ms))
            # current_cost += cost
            for x, y in zip(rs, ms):
                current_cost += abs(x - y)
        min_cost = min(current_cost, min_cost)

    return min_cost


s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
print(formingMagicSquare(s))