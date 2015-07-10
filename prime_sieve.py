import numpy as np

is_prime = np.ones((1000,),'bool')
is_prime[:2] = 0
N_max = int(np.sqrt(len(is_prime)))
n = N_max**2
for j in range(2,N_max):
    
    is_prime[j*j::j]=False
    
print np.nonzero(is_prime)