def find_in_a_sorted_array(L, key):
    length = len(L)
    s1 = 0
    e1 = length - 1
    pivot = find_pivot(L, s1, e1)
    pv = L[pivot]
    if key == pv:
        index = pivot
    elif key > pv:
        index = find_index(L, s1, pivot - 1, key)
    else:
        index = find_index(L, pivot + 1, e1, key)

    print('Index %d' % index)
    return index


def find_index(L1, s, e, key):
    l1 = e - s + 1
    h = int(l1 / 2 + s)
    if key == L1[h]:
        return h
    elif key > L1[h]:
        return find_index(L1, h + 1, e, key)
    else:
        return find_index(L1, s, h - 1, key)


def find_pivot(L2, s, e):
    # s: starting point
    # e: ending point
    # h: half

    l2 = e - s + 1
    a = L2[s]
    b = L2[e]
    h = int(l2 / 2 + s)
    c = L2[h]
    if l2 == 3:
        if a < c:
            return e
        else:
            return h

    if c > a:
        return find_pivot(L2, h - 1, e)
    else:
        return find_pivot(L2, s, h)

