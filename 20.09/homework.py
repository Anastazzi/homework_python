set_1 = {1, 2, 3, 4, 5, 6, 7, 6, 6 ,5, 5}
set_2 = {5, 6, 7, 8, 9, 0}
set_11 = [1, 2, 3, 4, 5, 6]
set_22 = [5, 6, 7, 8, 9, 0]

def unique(spis):
    return list(set(spis))

def intersec(set1, set2):
    return list(set(set1).intersection(set(set2)))

print(unique(set_1))
print(intersec(set_11, set_22))
