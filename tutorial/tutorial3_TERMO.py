########## TUTORIAL 3 ##########

# 1 - COMANDO FOR
# O comando "for" serve para fazer loops.
#Define-se a variável que variará ao longo do loop, ou seja, será a variável
# que controlará o andamento do loop. No caso abaixo, esse será o papel da variável "i".
#Utiliza-se o comando "in range" para definir qual o intervalo em que "i" variará.
#CUIDADO: o loop termina assim que "i" chega no limite superior,
#ou seja, o ação no interior do loop não é realizada para i = limite superior.
#Em outras palavras, o comando for fará o seguinte:
#"Para "i" variando de 0 a 10, faça o que está definido abaixo."
for i in range(0,10):
    print(i)
#O que será feito no loop é delimitado pela identação,
#assim como feito no caso das funções.


# 2 - COMANDO IF
#O comando "if" serve para fazer testes lógicos.
a = 2
if(a == 10): #Se o teste for verdadeiro, faça o que está abaixo
    print('A variável é igual a 10')
elif(a > 6): #Se o teste anterior der "falso", faça esse teste. Se der certo, faça o comando abaixo.
    print('A variável é maior que 3')
elif(a < 2): #Se os testes anteriores derem "falso", faça esse teste. Se der certo, faça o comando abaixo.
    print('A variável é menor que 2')
elif(a >=4): #Se os testes anteriores derem "falso", faça esse teste. Se der certo, faça o comando abaixo.
    print('A variável é maior ou igual a 4, porém, menor ou igual a 6')
else: #Se todos os testes acima derem "falso",  faça o comando abaixo.
    print('O número é maior ou igual a 2 e menor que 4.')

#Para realizar os testes lógicos, será preciso utilizar os seguintes operadores lógicos:
# x > y ---> x é maior que y?
# x < y ---> x é menor que y?
# x >= y ---> x é maior ou igual a y?
# x <= y ---> x é menor ou igual a y?
# x == y ---> x é igual a y?
# x != y ---> x é diferente de y?