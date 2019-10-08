########## TUTORIAL 1 ##########
# 1 - COMENTÁRIOS
#Qualquer linha iniciada por um "#" torna-se um comentário.


# 2 - DEFINIÇÃO DE VARIÁVEIS
#Definimos variáveis da seguinte forma:
A = 1
a = 2.3
#No python, letras maiúsculas e minúsculas representam variáveis diferentes!! Cuidado!!
#(diz-se que a linguagem é "case sensitive")
#Número decimais são escritos com ponto, não com vírgula.

aa = 1.2e-2 #Isso significa 1.2 vezes 10 elevado a -2.

# 3 - FUNÇÕES
#Para definir uma função, utilizamos o termo "def". O conjunto de ações que será
#realizado dentro da função deverá ser delimitado por meio de
#identação, que é o nome dado ao espaçamento antes da linha de texto começar.
def minha_func1():
    print(a) #Essa função imprime seu argumento na tela.

#Tente rodar essa função. Note que ela é capaz de acessar variáveis que estão fora dela.

#Se eu quiser termais controle sobre isso, posso definir explicitamente um argumento de entrada para a função.
def minha_func2(a):
    print(a)

def minha_func3(b):
    print(b)
#O nome dado a essa variável não precisa ter absolutamente nada a ver com os
#nomes das demais variáveis fora da função. Ao chamar a função, a variável
#inserida no argumento é automaticamente passada para o nome utilizado ao definir a função.
minha_func1()
minha_func2(a)
minha_func3(a)

#Dependendo do caso, pode-se desejar que a função retorne um valor.
#Para isso, utiliza-se o comando "return".
def minha_func_retorna1(a,b):
    return a+b

#A função anterior gera o mesmo resultado que a função a seguir:
def minha_func_retorna2(a,b):
    c = a + b #Posso criar variáveis dentro da função.
    #Quando a função terminar de rodar, essa variável é automaticamente deletada da memória.
    return c

#Chamando as funções:
d = minha_func_retorna1(a,A) #Quando a função retorna um valor,
e = minha_func_retorna2(a,A) #é necessário que uma variável o receba.
print('minha_func_retorna1 retornou ',d)
print('minha_func_retorna2 retornou ',e)

#Caso eu queira, posso retornar mais de um valor também.
def minha_func_retorna3(a,b):
    c = a**2 #Assim que se faz uma exponenciação
    return c, a+b

#Chamando a função
d,e = minha_func_retorna3(a,A)
print('minha_func_retorna3 retornou ',d,e)

