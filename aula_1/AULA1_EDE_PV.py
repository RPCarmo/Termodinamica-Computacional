#%%AULA 1 - TERMODINÂMICA
from scipy.constants import R
from math import exp
import numpy as np
import matplotlib.pyplot as plt

#INPUT
#Pentano
Pc = 33.7e5 #Pa
Tc = 469.7 #K
w = 0.252
A = 13.7667
B = 2451.88
C = 232.014

#Declaração de funções
def PR():
    sigma = 1 + 2**0.5
    epsilon = 1 - 2**0.5
    ac = 0.45724*(R*Tc)**2/Pc
    b = 0.0778*R*Tc/Pc
    kapa = 0.37464 + 1.54226*w - 0.26992*w**2
    return sigma,epsilon,ac,b,kapa
    
def PR_a(ac,kapa,Tr):
    return ac*(1+kapa-kapa*Tr**0.5)**2

def SRK():
    sigma = 0
    epsilon = 1
    ac = 0.42748*(R*Tc)**2/Pc
    b = 0.08664*R*Tc/Pc
    kapa = 0.48508 + 1.551171*w - 0.15613*w**2
    return sigma,epsilon,ac,b,kapa
    
def SRK_a(ac,kapa,Tr):
    return ac*(1+kapa-kapa*Tr**0.5)**2
    
def VDW():
    sigma = 0
    epsilon = 0
    ac = (27/64)*(R*Tc)**2/Pc
    b = R*Tc/(8*Pc)
    kapa = 0
    return sigma,epsilon,ac,b,kapa

def VDW_a(ac,kapa,Tr):
    return ac

def solve_cubica(sigma,epsilon,a,b,T,P):
    coef = np.zeros(4)
    #coef[0]*V**3 + coef[1]*V**2 + coef[2]*V + coef[3]
    coef[0] = 1
    coef[1] = (sigma+epsilon-1)*b-R*T/P
    coef[2] = sigma*epsilon*b**2-(R*T/P+b)*(sigma+epsilon)*b+a/P
    coef[3] = -(R*T/P+b)*sigma*epsilon*b**2-b*a/P
    raiz = np.roots(coef) #Resolvendo a cúbica
    
    if(np.all(abs(raiz.imag) < 1e-3)):
        Vv = np.amax(raiz.real)
        Vl = np.amin(raiz.real)
        if(Vl < b): Vl = Vv
    else:
        Vv = Vl = np.asscalar(np.real(raiz[np.isreal(raiz)]))

    return Vl,Vv

#Correlação para curva de saturação líquido-vapor
def Antoine(T,A,B,C): #T em Kelvin
    return exp(A-B/(T-273.15+C))*1000 #P em Pa

#Cálculo do diagrama P-V
N = 10000
T = np.linspace(230,460,N)
Vv = np.zeros(N)
Vl = np.zeros(N)
P = np.zeros(N)
spr,epr,acpr,bpr,kpr = PR()
for i in range(0,N):
    P[i] = Antoine(T[i],A,B,C)
    apr = PR_a(acpr,kpr,T[i]/Tc)
    Vl[i],Vv[i] = solve_cubica(spr,epr,apr,bpr,T[i],P[i])

Vmin = bpr*1.1
Vmax = 1000*bpr
V = np.linspace(Vmin,Vmax,N)
P_Tc = np.zeros(N)
P_sc = np.zeros(N)
P_elv = np.zeros(N)
P_gi_Tc = np.zeros(N)
P_gi_sc = np.zeros(N)
P_gi_elv = np.zeros(N)
apr_Tc = PR_a(acpr,kpr,Tc/Tc)
apr_sc = PR_a(acpr,kpr,(1.1*Tc)/Tc)
apr_elv = PR_a(acpr,kpr,298/Tc)
for i in range(0,N):
    P_Tc[i] = R*Tc/(V[i]-bpr)-apr_Tc/((V[i]+spr*bpr)*(V[i]+epr*bpr))
    P_sc[i] = R*1.1*Tc/(V[i]-bpr)-apr_sc/((V[i]+spr*bpr)*(V[i]+epr*bpr))
    P_elv[i] = R*298/(V[i]-bpr) - apr_elv/((V[i]+spr*bpr)*(V[i]+epr*bpr))
    P_gi_Tc[i] = R*Tc/V[i]
    P_gi_sc[i] = R*1.1*Tc/V[i]
    P_gi_elv[i] = R*298/V[i]

#PASSANDO AS PRESSÕES DE Pascal PARA bar
P = P/1e5
P_sc = P_sc/1e5
P_gi_sc = P_gi_sc/1e5
P_Tc = P_Tc/1e5
P_gi_Tc = P_gi_Tc/1e5
P_elv = P_elv/1e5
P_gi_elv = P_gi_elv/1e5
Pc = Pc/1e5

#GRÁFICOS
#Supercrit
plt.figure(1)    
plt.plot(np.log(Vv),P,'r-',label='Vap.Sat.')
plt.plot(np.log(Vl),P,'b-',label='Liq.Sat.')
plt.plot(np.log(V),P_sc,'k--',label='Supercrit.')
plt.plot(np.log(V),P_gi_sc,'g--',label='G.I.')
plt.legend()
plt.ylim(0,1.5*Pc)

#Crit
plt.figure(2)
plt.plot(np.log(Vv),P,'r-',label='Vap.Sat.')
plt.plot(np.log(Vl),P,'b-',label='Liq.Sat.')
plt.plot(np.log(V),P_Tc,'k-.',label='Crit.')
plt.plot(np.log(V),P_gi_Tc,'g-.',label='G.I.')
plt.legend()
plt.ylim(0,1.5*Pc)

#ELV
Vl_P20,_ = solve_cubica(spr,epr,apr_elv,bpr,298,20e5)
plt.figure(3)
plt.plot(np.log(Vv),P,'r-',label='Vap.Sat.')
plt.plot(np.log(Vl),P,'b-',label='Liq.Sat.')
plt.plot(np.log(V),P_elv,'k-',label='ELV')
plt.plot(np.log(V),P_gi_elv,'g-',label='G.I.')
plt.scatter(np.log(Vl_P20),20)
plt.legend()
plt.ylim(0,1.5*Pc)

#experimental
P_exp = np.array([0.69,1.38,2.07,2.76,3.45,4.14,4.83,5.52,6.21,6.89])
Vv_exp = np.array([0.034727,0.018107,0.012319,0.009351,0.007531,0.006297,0.005400,0.004720,0.004193,0.003770])
Vl_exp = np.array([0.000116,0.000120,0.000123,0.000125,0.000128,0.000130,0.000132,0.000133,0.000135,0.000137])
plt.figure(4)
plt.plot(np.log(Vv),P,'r-',label='Vap.Sat.')
plt.plot(np.log(Vl),P,'b-',label='Liq.Sat.')
plt.scatter(np.log(Vv_exp),P_exp)
plt.scatter(np.log(Vl_exp),P_exp)

plt.show()
    
    
    
    
    
