########## TUTORIAL 4 ##########
import numpy as np
import matplotlib.pyplot as plt
#O pacote matplotlib será útil para gerar gráficos.
#Nesse caso, estamos importando especificamente o pacote pyplot de dentro da biblioteca matplotlib.

x = np.linspace(0,10,20)
y = 1.2*x**2 + 1
#Para gerar um gráfico, basta utilizar o comando "plot", pertencente ao pyplot.
#plt.figure(1) #Ignore isso por enquanto
plt.plot(x,y)

#Se quisermos especificar coisas como a cor e o tipo da curva,
#a legenda e os limites dos eixos, precisamos usar alguns comandos extras.
#plt.figure(2) #Ignore isso por enquanto
plt.plot(x,y,'r-',label='Meu Plot') #O terceiro e quarto argumentos definem o
#                                   tipo de curva e o nome da legenda, respectivamente.
plt.legend() #Inclui no gráfico as legendas previamente definidas
plt.xlim(0,10) #Define os limites do eixo x
plt.ylim(0,100) #Define os limites do eixo y

#Se quiser plotar um único ponto, usa-se o comando "scatter"
#Vou plotar esse ponto no primeiro gráfico
#plt.figure(1) #Ignore isso por enquanto
plt.scatter(1,2) #ponto em x=1 e y=2

#Esse comando serve para que o python, após gerar os gráficos na memória, os mostre na tela.
#Escreva esse comando apenas após programados todos os gráficos que deseja-se gerar.
plt.show()

#Note que as duas curvas e o ponto foram plotadas no mesmo gráfico. Para que eles sejam
#geradas em gráficos distintos, é preciso usar o comando "figure", responsável
#por inicializar um novo gráfico. Para isso, basta retirar os "#" do início das linhas 10, 15 e 24.

