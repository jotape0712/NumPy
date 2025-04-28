
import numpy as np

dado = np.loadtxt('apples_ts.csv',delimiter=",", usecols=np.arange(1, 88,1)) # Carrega a tabela "apples_ts.csv" a partir da coluna 1 até a 87, de 1 em 1. 
# (Também pode ser carregado via URL.)

print(dado.ndim) # "ndim" usado para descobrir quantas dimensões tem os dados, nesse caso a saída será 2 (2d: Linhas e colunas).
print(dado.size) # "size" usado para ver a quantidade de elementos contidos na tabela.
print(dado.shape) # "Shape" mostra a quantidade de linhas e colunas contidas na tabela. 
print(dado.T) # "T" em maisculo, realiza a transposição da tabela, transformando as linhas em colunas, facilitando a compreensão dos dados.




