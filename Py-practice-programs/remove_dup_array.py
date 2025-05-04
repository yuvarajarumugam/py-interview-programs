def duplicate_array(lists: list):
    for i in range(len(lists)):
        for j in range(len(lists)):
            if i != j:
                if lists[i] == lists[j]:
                    lists[i] = 'del'

    while True:
        if 'del' in lists:
            lists.remove('del')
        else:
            break

    return lists

print(duplicate_array([1, 1, 2, 2, 3, 4, 4, 5, 1, 3, 1]))

