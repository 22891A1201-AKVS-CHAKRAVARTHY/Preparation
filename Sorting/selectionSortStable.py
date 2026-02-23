def selectionSortStable(a):
    if len(a) < 2:
        return a
    
    n = len(a)
    for i in range(n-1):
        min = i 
        for j in range(i+1, n):
            if a[min] > a[j]:
                min = j 
        
        tmp = a[min]
        
        while min > i:
            a[min] = a[min - 1]
            min -= 1
        a[i] = tmp

if __name__ == '__main__':
    l = [2,1,4,3,5,-1,0]
    print('Before Sorting:', l)
    selectionSortStable(l)
    print('After Sorting:', l)