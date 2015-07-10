import time as tt
import random as rd
def quicksort(array):
    
    if len(array)<2:
        return array
    
    pivot=rd.choice(array)
    n=array.index(pivot)
    array.remove(pivot)
    lower=[]
    upper=[]
    l=0
    u=0
    for index, item in enumerate(array):
        if item<pivot:
            lower.insert(l,item)
            l+=1
        else:
            upper.insert(u,item)
            u+=1
    abc=quicksort(lower)
    xyz=quicksort(upper)
    result = abc+[pivot]+xyz
    return result

a=rd.sample(xrange(100000), 50000)
st=tt.time()
print quicksort(a)
et= tt.time()-st
a=['x','e','t','q']
print quicksort(a)
a=["Arun","Anand","Geejo"]
print quicksort(a)
print"\n Time for sorting numeric array %f sec"%et