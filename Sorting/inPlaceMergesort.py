def merge(a,l,r,m):
    i, j, tmp = l, m+1, []
    
    while (i < m+1) and (j < r+1):
        if a[i] < a[j]:
            i += 1
        else:
            tmp = a[j]
            k = j
            while k > i:
                a[k] = a[k-1]
                k -= 1
            a[i] = tmp
            j += 1
            i += 1
            m += 1
            
def inPlaceMergeSort(a, left, right):
    if left >= right:
        return
    
    mid = (left + right) // 2
    inPlaceMergeSort(a, left, mid)
    inPlaceMergeSort(a, mid + 1, right)
    merge(a, left, right, mid)

if __name__ == '__main__':
    l = [2,1,4,3,5,-1,0]
    print('Before Sorting:', l)
    inPlaceMergeSort(l, 0, len(l) - 1)
    print('After Sorting:', l)