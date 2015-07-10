from scipy import misc
import numpy as np
import pylab as plt
lena = misc.lena()
lena.shape

lena = misc.lena()
plt.imshow(lena)
plt.show()
plt.imshow(lena,cmap=plt.cm.gray)
plt.show()
crop_lena = lena[30:-30,30:-30]
plt.imshow(crop_lena,cmap=plt.cm.gray)
plt.show()
y, x = np.ogrid[0:512,0:512] # x and y indices of pixels
y.shape, x.shape
centerx, centery = (256, 256)
mask = (((y - centery)**2)/121 + ((x - centerx)**2))/100 > 230**2 
lena[mask] = 0
plt.imshow(lena, cmap=plt.cm.gray)
plt.show()

y, x = np.ogrid[0:512,0:512] # x and y indices of pixels
mask2 = ((y - centery)/(200.0/256))**2 + ((x - centerx)/(129.0/256))**2 > 300**2
lena = misc.lena()
lena[mask2]=0
plt.imshow(lena,plt.cm.gray)
plt.show()
