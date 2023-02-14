lst = [[1,2,3],[1,2,3]]

for items in lst:
    for item in items:
        if item == 2:
            item = 0
        print(item)