def merge(a, l, r, m):
    i, j, tmp = l, m+1, []
    
    while (i < m+1) and (j < r+1):
        if a[i] < a[j]:
            tmp += [a[i]]
            i += 1
        else:
            tmp += [a[j]]
            j += 1
    
    while (i < m+1):
        tmp += [a[i]]
        i += 1
        
    while (j < r+1):
        tmp += [a[j]]
        j += 1
    
    for i in range(l,r+1):
        a[i] = tmp[i-l]
        
def mergeSort(a, left, right):
    if left >= right:
        return
    
    mid = (left + right)//2
    mergeSort(a, left, mid)
    mergeSort(a, mid + 1, right)
    merge(a, left, right, mid)
    

if __name__ == '__main__':
    l = [2,1,4,3,5,-1,0]
    print('Before Sorting:', l)
    mergeSort(l, 0, len(l) - 1)
    print('After Sorting:', l)