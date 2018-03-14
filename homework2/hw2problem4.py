

def mixed_sort(alist,threshold_k):
   sort_helper(alist,0,len(alist)-1,threshold_k)

def sort_helper(alist,first,last,k):
   if first<last:
       if last-first>=k:
           splitpoint = partition(alist,first,last)
           sort_helper(alist,first,splitpoint-1,k)
           sort_helper(alist,splitpoint+1,last,k)
       else:
           insertsrot(alist)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark


def insertsrot(alist):

    for i in range(len(alist)):
        j = i
        while j > 0 and alist[j - 1] > alist[j]:
            a =  alist[j]
            alist[j] = alist[j-1]
            alist[j-1] = a
            j = j-1



