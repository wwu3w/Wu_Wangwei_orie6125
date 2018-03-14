import numpy as np

def find_in_a_sorted_array(L,key):
    length = len(L)
    pivot = find_pivot(L)
    pv = L[pivot]
    f = L[0]
    l = L[length-1]
    if key == pv:
        return pivot
    elif key > pv:
        L1 = [L(i) for i in range(pivot)]
        return find_index(L1,key)
    else:
        L1 = [L(i) for i in range(pivot+1,length)]
        return pivot+1+find_index(L1,key)

def find_index(L,key):
    l1 = len(L1)
    p = np.floor(l1 / 2)
    if key == L1(p):
        return p
    elif key > pv:
        L1 = [L(i) for i in range(p)]
        return find_index(L1,key)
    else:
        L1 = [L(i) for i in range(p+1,l1)]
        return p+1+find_index(L1,key)

def find_pivot(L2):
    l2 = len(L2)
    a = L2[0]
    b = L2[l2-1]
    p = np.floor(l2/2)
    c = L2(p)
    if l2 == 3:
        if a < c:
            return 1
        else:
            return 2

    if c > a:
        L3 = [L2(i) for i in range(p-1,length)]
        return p-1+find_pivot(L3)
    else:
        L3 = [L2(i) for i in range(0, p+1)]
        return find_pivot(L3)
