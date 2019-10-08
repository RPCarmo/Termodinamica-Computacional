import numpy as np
import EDE_new as EDE
import matplotlib.pyplot as plt
from scipy.constants import R

#Butano
Tc = 425.1 #K
Pc = 37.96e5 #Pa
w = 0.2

#Coeficientes de Antoine
A = 13.6608
B = 2154.7
C = 238.789

#Calculando variáveis da Equação de estado
N = 1000
T = np.linspace(150,420,N)
sigma,epsilon,ac,b,kapa = EDE.PR(Tc,Pc,w)
a = EDE.PR_a(ac,kapa,T/Tc)
dadt = EDE.PR_dadt(a,kapa,Tc,T)

P = np.zeros(N)
Vl = np.zeros(N)
Vv = np.zeros(N)

#Primeiro ponto
P0 = 1
P[0],Vl[0],Vv[0] = EDE.calc_eq(T[0],P0,epsilon,sigma,a[0],b,dadt[0])
##Demais pontos
for i in range(1,N):
    P[i],Vl[i],Vv[i] = EDE.calc_eq(T[i],P[i-1],epsilon,sigma,a[i],b,dadt[i])


P_ant = EDE.Antoine(T,A,B,C)

#DIAGRAMA P-T
plt.figure(1)
plt.plot(T,P_ant,label='Antoine')
plt.plot(T,P,label='EdE')
plt.legend()

#%%DIAGRAMA P-H
#Contribuicao da variacao de entalpia de gas ideal
Cp_a = 1.935
Cp_b = 36.915*1e-3
Cp_c = -11.402*1e-6
T0 = 298 #K
#Integral de Cp*dT de T0 a T
Hgi = R*((Cp_a*T+Cp_b*T**2/2+Cp_c*T**3/3) - (Cp_a*T0+Cp_b*T0**2/2+Cp_c*T0**3/3))
#Contribuicao da entalpia residual
Hr_v = EDE.Hresidual(epsilon,sigma,a,b,dadt,P,Vv,T)
Hr_l = EDE.Hresidual(epsilon,sigma,a,b,dadt,P,Vl,T)

dH_l = Hgi + Hr_l
dH_v = Hgi + Hr_v

T1 = 350
a1 = EDE.PR_a(ac,kapa,T1/Tc)
dadt1 = EDE.PR_dadt(a1,kapa,Tc,T1)
V1 = np.logspace(np.log10(1.1*b),np.log10(5e5*b),N)
P1 = EDE.P_ede(T1,V1,sigma,epsilon,a1,b)
Hgi1 = R*((Cp_a*T1+Cp_b*T1**2/2+Cp_c*T1**3/3) - (Cp_a*T0+Cp_b*T0**2/2+Cp_c*T0**3/3))
Hr1 = EDE.Hresidual(epsilon,sigma,a1,b,dadt1,P1,V1,T1)
dH1 = Hgi1 + Hr1

T2 = 450
a2 = EDE.PR_a(ac,kapa,T2/Tc)
dadt2 = EDE.PR_dadt(a2,kapa,Tc,T2)
V2 = np.logspace(np.log10(1.1*b),np.log10(5e5*b),N)
P2 = EDE.P_ede(T2,V2,sigma,epsilon,a2,b)
Hgi2 = R*((Cp_a*T2+Cp_b*T2**2/2+Cp_c*T2**3/3) - (Cp_a*T0+Cp_b*T0**2/2+Cp_c*T0**3/3))
Hr2 = EDE.Hresidual(epsilon,sigma,a2,b,dadt2,P2,V2,T2)
dH2 = Hgi2 + Hr2

plt.figure(2)
plt.plot(dH_v,P,'r-',label='Vap.Sat.')
plt.plot(dH_l,P,'b-',label='Liq.Sat.')
plt.plot(dH1,P1,'g-',label='T=350')
plt.plot(dH2,P2,'m-',label='T=450')
plt.ylim(1e2,1e9)
plt.yscale('log')
plt.legend()






