'''
Anotações da aula 07 de python
Operadores aritméticos

'''
#region operações aritméticas
'''
pricipais operadores aritméticos

operadores binários (precisam de dois atributos numéricos)

'+' -- adição
'-' -- subtração
'/' -- divisão
'**' -- potência
'//' -- divisão inteira (retorna o número inteiro de uma divisão)
'%' -- resto da divisão (retorna o resto de uma divisão inteira)

ex: 5/2 = 
      5 | 2 
    - 4  (2) divisão inteira
     (1) resto da divisão
      
obs: o sinal de igual é dado por '==' e não '=' que significa atribuição

ordem de precedência:
1: ()
2: **
3: *, /, //, % -- ordem linear
4: +,- 

'''


print('a ordem de precedência prevalece sobre a linearidade como podemos observar nos seguintes casos\n')
numero = 5 + 3 * 2
print('5 + 3 * 2 = {}'.format(numero))
numero = 3 * 5 + 4 ** 2
print('3 * 5 + 4 ** 2 = {}'.format(numero))


#ex:
print('\nexemplo: desejamos resolver a operação 5+3 e depois multiplicar por 2\n')

print('quando não nos atentamos a ordem de precedência podemos ter problems ')
numero = 5 + 3 * 2
print('( 5 + 3 ) * 2 ={}'.format(numero))

print('\ncomo o programa segue uma linearidade e ordem de precedência nem todos as operações serão realizadas como o desejado')
print('para resolução do problema usaremos parênteses para evitar ambiguidades')
numero = ( 5 + 3 ) * 2
print('( 5 + 3 ) * 2 = {}'.format(numero))

#endregion

#region extra: funções print
print('\n\nextra: format print\n')
mensagem = input('digite algo ')
print('{:20}!'.format(mensagem)) # limita o número de caracteres
print('{:>20}!'.format(mensagem)) # limita o número de caracteres e direciona o texto para a direita
print('{:<20}!'.format(mensagem)) # limita o número de caracteres e direciona o texto para a esquerda
print('{:^20}!'.format(mensagem)) # limita o número de caracteres e centraliza o texto
print('{:=^20}!'.format(mensagem)) # limita o número de caracteres, centraliza o texto e preenche o texto com o caractere dado

print('\n exemplo: fazer a soma multiplicação e divisão de dois números do usuário\n')
n1 = int(input('n1 = '))
n2 = int(input('n2 = '))
soma = n1+n2
multiplicacao = n1*n2
divisao = n1/n2
print('n1+n2 = {}'.format(soma), end=' ')
print('n1*n2 = {}'.format(multiplicacao), end=' ')
print('n1/n2 = {:.3f}'.format(divisao)) # garante a exibição de apenas 3 números após a virgula, com arredondamento

#endregion