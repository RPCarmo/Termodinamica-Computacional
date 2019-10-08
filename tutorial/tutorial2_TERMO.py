########## TUTORIAL 2 ##########

# 1 - IMPORTAR PACOTES
#Podemos precisar de recursos presentes em bibliotecas.
#Para incluí-los no programa, precisamos usar o comando "import".
import numpy as np
#Como precisaremos utilizar esse nome o tempo todo,
#usamos o comando "as" para criar um apelido menor e mais simples.
#O pacotre numpy será útil para utilização de arrays 


# 2 - INICIALIZAÇÃO DE ARRAYS
#Arrays são variáveis armazenadas de forma sequencial. São análogas ao que
#conhecemos como vetor. A diferença é que existe uma série de operações,
#como produto escalar e produto vetorial, para vetores, as quais não se estendem aos arrays.

#Inicializando arrays
a1 =np.zeros(5) #Um array de 5 elementos contendo o valor zero.
print('a1 é ',a1)
a2 = np.array([1,2,3]) #Um array contendo os elementos listados
print('a2 é ',a2)
a2d = np.zeros([2,2]) #Posso criar um array bidimensional também.
print('a2d é ',a2d)


# 3 - UTILIZANDO ARRAYS
a1 = a1+2 #Somei 2 em todos os elementos de a1
print('a1 agora vale ',a1)
a1[0] = a1[0]*3 #Multipliquei o primeiro elemento do array por 3
print('O primeiro elemento de a1 agora vale ',a1[0])
#Diferentemente do que faríamos ao contar os elementos de um vetor
#na vida real, a contagem dos elementos de um array começa em zero.
#Para acessar, um array bidimensional, é assim:
a2d[0,1] = 1.234 #Mudando o elemento da linha 1 coluna 2
print('a2d agora vale ',a2d)

#Posso fazer operações utilizando apenas uma parte do array. Para isso, basta usar ":".
a2[1:] = a2[1:]*2 #Multipliquei por 2 apenas a partir do segundo elemento.
print('a2 agora vale ',a2)
#Quando estivermos trabalhando co índices de arrays, ao utilizar ":" depois
#de um número, como no caso anterior, significa "todos os elementos a partir desse aqui".
#Quando utilizado antes (Ex: a2[:1]), significa "todos os elementos até esse daqui"
#Sendo assim, podemos usar ":" para selecionar qualquer fragmento de um array.

#Podemos criar uma array contendo N elementos,
#indo de um limite inferior a um superior, da seguinte forma:
aaa = np.linspace(0,10,5) #Um array indo de 0 a 10 e contendo 5 elementos.
print('aaa é igual a ',aaa)






