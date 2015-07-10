import time as tt
st=tt.time()
print "This is console module"
a=1.0
for i in range(1,1000000):
    b=4.0*i**2
    a=((b)/(b-1))*a
a=a*2.0
print ("Pi is %f"%(a))
print tt.time()-st