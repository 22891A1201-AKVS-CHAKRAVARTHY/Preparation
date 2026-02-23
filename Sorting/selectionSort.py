def selectionSort(a):
    if len(a) < 2:
        return a
    
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if a[min] > a[j]:
                min = j
        
        a[i], a[min] = a[min], a[i]
    
if __name__ == '__main__':
    l = [2,1,4,3,5,-1,0]
    print('Before Sorting:', l)
    selectionSort(l)
    print('After Sorting:', l)