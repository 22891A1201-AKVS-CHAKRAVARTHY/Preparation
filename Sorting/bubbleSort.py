def bubbleSort(a):
    if len(a) < 2:
        return a
    
    n = len(a)
    for i in range(n-1):
        c = 0
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                c = 1
        if not c:
            break
    
if __name__ == '__main__':
    l = [2,1,4,3,5,-1,0]
    print('Before Sorting:', l)
    bubbleSort(l)
    print('After Sorting:', l)