def pivotPlace(a, l, r):
    pivot = a[l]
    i, j = l, r

    while i < j:
        while (i <= r) and (a[i] <= pivot):
            i += 1
        
        while (j >= l) and (a[j] > pivot):
            j -= 1
        
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]

    return j

def quickSort(a, l, r):
    if l < r:
        partitionIndex = pivotPlace(a, l, r)
        quickSort(a, l, partitionIndex - 1)
        quickSort(a, partitionIndex + 1, r)
        

if __name__ == '__main__':
    l = [2,1,4,3,5,-1,0]
    print('Before Sorting:', l)
    quickSort(l, 0, len(l) - 1)
    print('After Sorting:', l)