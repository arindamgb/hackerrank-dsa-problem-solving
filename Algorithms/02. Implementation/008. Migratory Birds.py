# https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    # Write your code here
    arr_set = set(arr)
    bird_types = list(arr_set)
    # print(bird_types)
    counts = dict()

    for bird in bird_types:
        counts[bird] = 0
    # print(counts)

    for bird in arr:
        counts[bird] += 1
    # print(counts)

    max_sighting = (max(zip(counts.values())))[0]
    # print(max_sighting)

    max_sighted_birds = []
    for k, v in counts.items():
        if v == max_sighting:
            max_sighted_birds.append(k)

    # print(max_sighted_birds)
    # print(min(max_sighted_birds))

    return min(max_sighted_birds)








arr = [1, 1, 2, 2, 3]
# arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

print(migratoryBirds(arr))