"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
def print_words(filename): #essa função printa em ordem alfabética as palavras ou letras que aparecerem e na frente o número de vezes que apareceram
    with open(filename,'r') as arquivo: #abre o arquivo filename.txt e atribui ele ao objeto arquivo
        palavras = arquivo.read().lower().split() #lista de palavras do arquivo em minúsculo e separadas uma por uma. Aqui no caso vamos separar letra por letra
        dicionario = dict() #dicionário vazio, ele vai conter mais pra frente o resultado

        for palavra in palavras: #palavra percorre a lista palavras
            if palavra in dicionario: #se a palavra atual existe como chave no dicionário
                dicionario[palavra] += 1 #então aquela chave recebe mais 1
            else: #senão existe
                dicionario[palavra] = 1 #ela é criada e recebe o valor 1
        
        #Items cria uma lista de tuplas através de um dicionário, assim: (chave do dicionário, valor do dicionário)
        for chave,valor in dicionario.items(): #chave e valor vão percorrer uma lista de tuplas, sendo chave o primeiro elemento da tupla e valor o segundo
            print(chave + ' ' + str(valor)) #printa o resultado com um espaço entre eles. 

def print_top(filename): #essa função printa as 20 letras que mais apareceram em um arquivo de texto
    #aqui fazemos exatamente como acima
    with open(filename,'r') as arquivo: 
        palavras = arquivo.read().lower().split() 
        dicionario = dict()

        for palavra in palavras:
            if palavra in dicionario:
                dicionario[palavra] += 1
            else:
                dicionario[palavra] = 1
        
        #mudamos aqui:
        for chave,valor in sorted(dicionario.items(),key=lambda x:x[1],reverse=True)[:20]: #chave e valor vão percorrer uma lista de tuplas como acima, porém a lista será ordenada a partir do segundo elemento de cada tupla, até os 20 primeiros elementos
            print(chave + ' ' + str(valor)) #mostra o resultado pra gente

# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
