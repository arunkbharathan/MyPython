codeword = 0b10000000000000000011111100
offsetword =               0b0011111100
Si=0
Sf=0
Reg16=0
Ga=1
Gb=1
Gc=0
outword=0
from pudb import set_trace
for i in xrange(32):
    
    if(i==16):
        Gb=0
        Gc=1
    
    inbit=(codeword & (33554432>>i))>0
    if(Gc):
        inbit = inbit^((offsetword&(512>>(i-16)))>0)
    set_trace()
    MSB=(Si&512)>0
    a=0
    b=0
    c=0
    if(MSB&Ga):
        a=441
    if(inbit):
        b=795
    c=(Si&477)<<1
    Sf=(a^b)
    Sf=Sf^c
    
    
    multiNOR=not((Si&31)>0)
    dualAND=MSB&multiNOR
    
    if(multiNOR&(i>15)):
        Ga=0
        
    
    RegOutbit=(((Reg16<<1)&65536)>0)
    Reg16=(Reg16<<1)&65535
    if(Gb&inbit):
        Reg16^=1
    
    
        
    outbit=dualAND^RegOutbit
    outword=(outword<<1)^outbit
    
    #print i,' ',bin(Si),"@",bin(Sf),'@',bin(Reg16),'@',multiNOR,'@',MSB,'@',dualAND,'@',outbit,'@',bin(outword)
    #raw_input([""])
    Si=Sf

print '*',bin(outword)
if((Si&31)>0):
        print 'Bad Block'
