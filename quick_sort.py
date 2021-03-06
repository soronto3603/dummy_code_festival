from PIL import Image
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
    global f,l,im,px
    b=alist
    f=sorted(b)
    g=len(b)*2
    if(im==None):
        im=Image.new('RGB',(g,g))
        px=im.load()
    for i in range(len(f)):
        if(f[i] == b[i]):
            px[i,l]=(76,175,80)
        else:
            px[i,l]=(244,67,54)
    
    if start < end:
        
        pivot = partition(b, start, end)
        px[start,l]=(103,58,183)
        px[pivot,l]=(103,58,183)
        px[end,l]=(103,58,183)
        l=l+1
        quickSort(b, start, pivot-1)
        quickSort(b, pivot+1, end)
        
    im.save("1.png")
    return b
l=0
im,px=None,None
