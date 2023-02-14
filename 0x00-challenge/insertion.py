#!/usr/bin/env python3

data = [12, 41, 2, 9, -9, 31, -1, 32]

result = []
for j in range(len(data)):
    is_inserted = False
    i = 0
    l = len(result)
    while not is_inserted and i < l:
        if data[j] > result[i]:
            i = i + 1
        else:
            result.insert(i, data[j])
            is_inserted = True
    if not is_inserted:
        result.append(data[j])
print(result)
