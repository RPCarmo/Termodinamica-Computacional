import EDE_new as EDE

T = 350 #K (77 ºC)
#T = 355 #K (82 ºC)
P = 10 #bar
P = P*1e5 #bar -> Pascal

#Butano
Tc = 425.1 #K
Pc = 37.96e5 #Pa
w = 0.2

#Calculando variáveis da Equação de estado
sigma,epsilon,ac,b,kapa = EDE.PR(Tc,Pc,w)
a = EDE.PR_a(ac,kapa,T/Tc)
dadt = EDE.PR_dadt(a,kapa,Tc,T)

#Encontrando as raízes de volume
Vl,Vv = EDE.solve_cubica(sigma,epsilon,a,b,T,P)

#Calculando G residual para as duas fases
Gr_l = EDE.Gresidual(epsilon,sigma,a,b,dadt,P,Vl,T)
Gr_v = EDE.Gresidual(epsilon,sigma,a,b,dadt,P,Vv,T)

print('Vapor',Gr_v)
print('Líquido',Gr_l)

#Experimental: P = 10 bar -> Tsat ~ 80ºC = 353 K







