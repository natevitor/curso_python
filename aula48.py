"""
Listas em Python 
Tipo list - Mutavel 
Suporta varios valores de qualquer tipo 
Conhecimentos reutilizaveis - indices e fatiamento 
metodos uteis : 
    append - Adiciona um item ao final 
    insert - Adiciona um item no indice escolhido 
    pop - Remove do final ou do indice escolhido 
    del - Apaga um indice 
    clear - Limpa a lista 
    extend - Estende a lista 
    + - concatena listas 
Create Read Update Delete
Criar, Ler, alterar, apagar = lista[i] (CROUD)
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

"""garbage collector". Um "garbage collector" (coletor de lixo, em português) é um 
componente de um sistema de gerenciamento de memória usado em linguagens de programação 
que possuem alocação dinâmica de memória, como Java, Python, JavaScript, entre outras."""

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
