
import numpy as np

def max_subarray(L):
    if L == []:
        return 'Empty'
    length = len(L)
    d, index = difference(L,length)
    max = np.max(index[:,1]-index[:,0])
    b = [k for k in range(2 * length) if index[k, 1] - index[k, 0] == max]
    result = np.zeros((len(b),2))
    for i in range(len(b)):
        if i == 0:
            print ("%d to %d" % (index[b[i],0],index[b[i],1]-1))
        else:
            print (" Or %d to %d" % (index[b[i], 0], index[b[i], 1] - 1))
        result[i,:] = [index[b[i],0],index[b[i],1]-1]
    return result


def difference(L, length):
    d = np.zeros(length + 1)
    z = np.zeros(2 * length)
    index = np.zeros((2 * length, 2))
    z[int(0 + length - 2)] = 1
    index[int(0 + length - 2), 0] = 0
    for i in range(length):
        if L[i] == L[0]:
            d[i + 1] = d[i] + 1
        else:
            d[i + 1] = d[i] - 1
        j = int(d[i + 1] + length - 2)
        if np.power(0, z[j]) == 1:
            z[j] = 1
            index[j, 0] = i + 1
            index[j, 1] = i + 1
        else:
            index[j, 1] = i + 1
    return d, index

