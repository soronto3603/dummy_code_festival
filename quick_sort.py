def partition(alist, start, end):
    pivot = alist[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and alist[left] <= pivot:
            left += 1
        while alist[right] >= pivot and right >= left:
            right -= 1
    if right < left:
            done = True
        else:
            tmp = alist[left]
            alist[left] = alist[right]
            alist[right] = tmp
    tmp = alist[start]
    alist[start] = alist[right]
    alist[right] = tmp
    return right
def quickSort(alist, start, end):
    if start < end:
        pivot = partition(alist, start, end)
        quickSort(alist, start, pivot-1)
        quickSort(alist, pivot+1, end)
    return alist