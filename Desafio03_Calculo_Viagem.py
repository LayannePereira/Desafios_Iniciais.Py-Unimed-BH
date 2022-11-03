# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
valores = input().split()
GASTO = 12

tempo = int(valores[0])
velocidade = int(valores[1])

distancia = velocidade*tempo

# Cálculo da quantidade de litros necessária para realizar a viagem
litros = float(distancia) / float(GASTO)

# Impressão com TRÊS dígitos após o ponto decimal
print(f'{litros:.3f}')
