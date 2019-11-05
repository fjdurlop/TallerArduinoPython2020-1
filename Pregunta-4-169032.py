import sys
import math

def xor(b1,b2):
    #b1 y b2 son int
    #xor es int
    if ((b1==1 and b2==1) or (b1==0 and b2==0)):
        return 0
    else:
        return 1
    #endIf
#endFunction

def binSum(A,B):
    #A y B son strings
    #Cy, S1 y S2 son int
    #binSum es int
    Suma=""
    Cy=0
    for i in range(31,-1,-1):
        S1=int(A[i:i+1])
        S2=int(B[i:i+1])
        if (xor(Cy,xor(S1,S2))==0):
            S="0"
        else:
            S="1"
        #endIf
        SS=Cy+S1+S2
        if (SS>=2):
            Cy=1
        else:
            Cy=0
        #endIf
        Suma=S+Suma
    #endFor
    return Suma	
#endFunction

def getDec(N):
#
#   N --> ASCII Binary String
#
#   RETURNS --> Float
#
    decnum=float(N[0:1])
    for i in range(1,32):
        decnum=decnum*2+float(N[i:i+1])
    #endFor
    decnum=decnum/_2_32
    return decnum
#endFunction
    
def Dec2Bin(numero):  #se define funcion Dec2Bin
    B=""
    for i in range (0,31):
        numero=numero*2
        if (numero>=1):
            B=B+"1"
            numero=numero-int(numero)
        else:
            B=B+"0"
        
            
            
    B=B+"1" #para que sea par
    return B
#
#   MAIN
#    
    
_2_32=2**32
pi_2=math.pi/2
RaizDecimal=float(0.7777)
Kbin=Dec2Bin(RaizDecimal)
while (True):
    N=10000
    l=10
    t=l
    h=0
    for i in range(N):
        _2Kbin=Kbin[1:32]+"0"                  # *2
        _3Kbin=binSum(Kbin,_2Kbin)		           # *3
        _64KKbin=Kbin[16:32]+"0000000000000000" # *65536
        Kbin=binSum(_3Kbin,_64KKbin)		        # *65539
        fKbin=getDec(Kbin) 
        x=fKbin*t/2
        _2Kbin=Kbin[1:32]+"0"                  # *2
        _3Kbin=binSum(Kbin,_2Kbin)		           # *3
        _64KKbin=Kbin[16:32]+"0000000000000000" # *65536
        Kbin=binSum(_3Kbin,_64KKbin)		        # *65539
        fKbin=getDec(Kbin) 
        theta=fKbin*pi_2
        if x<=(l/2)*(math.sin(theta)):
            h=h+1
        #endif
    #endfor
    PI=2*N/h
    print(PI)
    resp=input("Quiere continuar (S/N)\t").upper()
    if resp!="S":
        break
    #endIf
#endWhile
    
    