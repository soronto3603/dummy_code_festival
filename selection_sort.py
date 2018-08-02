from PIL import Image
def insertionSort(alist):
    b=alist
    a=len(b)
    im=Image.new('RGB',(a,a))
    px=im.load()
    
    for i in range(a-1):
        for j in range(i+1,a-1):
            px[j,i]=(76,175,80)
            if b[i] < b[j] :
                px[j,i]=(244,67,54)
                b[i],b[j]=b[j],b[i]
    im.save("1.png")
    return b

import random
c=[i for i in range(100000)]
d=random.sample(c,20)
insertionSort(d)