def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    leftlist = alist[:mid]
    rightlist = alist[mid:]
    L = mergeSort(leftlist)
    R = mergeSort(rightlist)
    i = j = 0
    result = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i+=1
        else:
            result.append(R[j])
            j+=1
    result += L[i:]
    result += R[j:]
    return result