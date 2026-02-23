def insertionSort(a):
    if len(a) < 2:
        return a
    
    n = len(a)
    for i in range(1, n):
        j = i
        
        while (j > 0) and (a[j] < a[j-1]):
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1

if __name__ == '__main__':
    l = [2,1,4,3,5,-1,0]
    print('Before Sorting:', l)
    insertionSort(l)
    print('After Sorting:', l)