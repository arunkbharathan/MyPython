# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

class Markov:
    
    def __init__(self):
        self.P = self.generate_P()
        self.p = self.generate_p()
        
    def generate_P(self):
        np.random.seed(24031988)
        P = np.random.rand(5,5)
        n=np.sum(P,axis=1)
        n=n[:,np.newaxis]
        return P/n
    
    def generate_p(self):
        np.random.seed(24032015)
        p=np.random.rand(5,1)
        n=np.sum(p)
        return p/n
    
    def findit(self):
        for j in range(1000):
            self.p=self.P.T.dot(p)
        #return self.get_p()
            
    def get_p(self):
        return self.p
    def get_P(self):
        return self.P

    
tolerance = 1e-5    
M=Markov()
#print M.get_p()
P=M.get_P()
p_ini=M.get_p()
#print np.linalg.norm(p_ini)
M.findit()
p_fin=M.get_p()
#print np.linalg.norm(p_fin)
a,b=np.linalg.eig(P.T)
b=np.real(b[:,0])[:,np.newaxis]
p_sta=b/b.sum()
# Compare
if all(abs(p_fin - p_sta) < tolerance):
    print "Tolerance satisfied in infty-norm"

if np.linalg.norm(p_fin - p_sta) < tolerance:
    print "Tolerance satisfied in 2-norm"

# <codecell>

a,b=np.linalg.eig

# <codecell>

np.sum(P, axis=1)-1

# <codecell>

p.sum() - 1

# <codecell>

P

# <codecell>

p

# <codecell>

np.dot(P,p)

# <codecell>

np.linalg.norm(P)

# <codecell>

np.sum(p**2)

# <codecell>


