#FUNCOES RELACIONADAS A EQUACOES DE ESTADO
from scipy.optimize import fsolve
from scipy.constants import R
import numpy as np

#Declaracao de funcoes
def P_ede(T,V,sigma,epsilon,a,b):
    return R*T/(V-b)-a/((V+sigma*b)*(V+epsilon*b))

def PR(Tc, Pc, w):
    sigma = 1 + 2**0.5
    epsilon = 1 - 2**0.5
    ac = 0.45724*(R*Tc)**2/Pc
    b = 0.0778*R*Tc/Pc
    kapa = 0.37464 + 1.54226*w - 0.26992*w**2
    return sigma,epsilon,ac,b,kapa
    
def PR_a(ac,kapa,Tr):
    return ac*(1+kapa-kapa*Tr**0.5)**2

def PR_dadt(a,kapa,Tc,T):
    return -a*kapa/Tc*((1+kapa)/(T/Tc)**0.5-kapa)

def SRK(Tc, Pc, w):
    sigma = 0
    epsilon = 1
    ac = 0.42748*(R*Tc)**2/Pc
    b = 0.08664*R*Tc/Pc
    kapa = 0.48508 + 1.551171*w - 0.15613*w**2
    return sigma,epsilon,ac,b,kapa
    
def SRK_a(ac,kapa,Tr):
    return ac*(1+kapa-kapa*Tr**0.5)**2

def SRK_dadt(a,kapa,Tc,T):
    return -a*kapa/Tc*((1+kapa)/(T/Tc)**0.5-kapa)
    
def VDW(Tc, Pc, w):
    sigma = 0
    epsilon = 0
    ac = (27/64)*(R*Tc)**2/Pc
    b = R*Tc/(8*Pc)
    kapa = 0
    return sigma,epsilon,ac,b,kapa

def VDW_a(ac,kapa,Tr):
    return ac

def VDW_dadt(a,kapa,Tc,T):
    return 0

def solve_cubica(sigma,epsilon,a,b,T,P):
    coef = np.zeros(4)
    #coef[0]*V**3 + coef[1]*V**2 + coef[2]*V + coef[3]
    coef[0] = 1
    coef[1] = (sigma+epsilon-1)*b-R*T/P
    coef[2] = sigma*epsilon*b**2-(R*T/P+b)*(sigma+epsilon)*b+a/P
    coef[3] = -(R*T/P+b)*sigma*epsilon*b**2-b*a/P
    raiz = np.roots(coef) #Resolvendo a cubica
    
    if(np.all(abs(raiz.imag) < 1e-3)):
        Vv = np.amax(raiz.real)
        Vl = np.amin(raiz.real)
        if(Vl < b): Vl = Vv
    else:
        Vv = Vl = np.asscalar(np.real(raiz[np.isreal(raiz)]))

    return Vl,Vv


#Correlacao para curva de saturacao li­quido-vapor
def Antoine(T,A,B,C): #T em Kelvin
    return np.exp(A-B/(T-273.15+C))*1000 #P em Pa


#PROPRIEDADES RESIDUAIS
def Hresidual(epsilon,sigma,a,b,dadt,P,V,T):
    if(epsilon != sigma):
        psi = np.log((V+epsilon*b)/(V+sigma*b))/(b*(epsilon-sigma))
    else:
        psi = 1/(V+sigma*b)
    
    return P*V - R*T + (T*dadt - a)*psi

def Sresidual(epsilon,sigma,b,dadt,P,V,T):
    if(epsilon != sigma):
        psi = np.log((V+epsilon*b)/(V+sigma*b))/(b*(epsilon-sigma))
    else:
        psi = 1/(V+sigma*b)
    return R*np.log(P*(V-b)/(R*T))+dadt*psi

def Gresidual(epsilon,sigma,a,b,dadt,P,V,T):
    Sr = Sresidual(epsilon,sigma,b,dadt,P,V,T)
    Hr = Hresidual(epsilon,sigma,a,b,dadt,P,V,T)
    return Hr - T*Sr


#EQUILIBRIO LIQUIDO-VAPOR
def calc_eq(T,P0,epsilon,sigma,a,b,dadt):
    
    def fres(P,T,sigma,epsilon,a,b,dadt):
        Vl,Vv = solve_cubica(sigma,epsilon,a,b,T,P)
        Gr_l = Gresidual(epsilon,sigma,a,b,dadt,P,Vl,T)
        Gr_v = Gresidual(epsilon,sigma,a,b,dadt,P,Vv,T)
        
        return Gr_l - Gr_v #função resíduo
    
    P = fsolve(fres,P0,args=(T,sigma,epsilon,a,b,dadt))
    
    Vl,Vv = solve_cubica(sigma,epsilon,a,b,T,P)
    
    return P, Vl, Vv







    
    
