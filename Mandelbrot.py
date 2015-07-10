# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

class mandelbrot:
    def __init__(self,N_max,some_threshold,c):
        self.N_max = N_max
        self.some_threshold = some_threshold
        self.c = c
    def findit(self):
        z=self.c
        for j in xrange(self.N_max):
            z = z**2 + c
        mandelbrot_set = (abs(z) < self.some_threshold)
        return mandelbrot_set
    
x,y = np.ogrid[-2:1:1001j,-1.5:1.5:1001j]
c=(x+1j*y)**11
#c = (1./(x +1j*y))**4
#c = x +1j*y
#c = x**2 +1j*2*x*y-y**2
#c = (1j*x-0.25)**2+y**2
a = mandelbrot(50,50.,c)
mandelbrot_set = a.findit()
plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])
plt.hot()
plt.savefig('mandelbrot.png')

# <codecell>

plt.imshow?

# <codecell>


