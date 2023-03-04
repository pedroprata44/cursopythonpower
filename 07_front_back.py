"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
from math import ceil

def dividir_string(s):
    i = ceil(len(s)/2) #calculando metade do tamanho da string em número inteiro utilizando o ceil

    if len(s) % 2 == 0: #se for par
        frente = s[:i]
        tras = s[i:]
        return [frente,tras] #retorna uma lista com duas partes da string, 0 = frente, 1 = tras

    #se não for par, então é impar
    frente = s[:i] #coloca o restante da string na frente
    tras = s[i:] 
    return [frente,tras] #retorna a lista com duas partes

def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    return dividir_string(a)[0] + dividir_string(b)[0] + dividir_string(a)[1] + dividir_string(b)[1]

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
