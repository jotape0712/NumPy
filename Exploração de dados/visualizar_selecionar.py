
import numpy as np
import matplotlib.pyplot as plt

dado = np.loadtxt('apples_ts.csv',delimiter=",", usecols=np.arange(1, 88,1)) # Carrega a tabela "apples_ts.csv" a partir da coluna 1 até a 87, de 1 em 1. 
# (Também pode ser carregado via URL.)


dado_transposto = dado.T # "T" em maisculo, realiza a transposição da tabela, transformando as linhas em colunas, facilitando a compreensão dos dados.

datas = dado_transposto[:,0]# ":" pega os dados de todas as linhas.
preços = dado_transposto[:,1:6] # Pega todas as linhas e puxa as colunas de 1 a 6, onde estão os preços.
datas = np.arange(1,88,1) # gerar um array contendo os números inteiros de 1 até 87 e incrementando de 1 em 1. 
# No contexto do gráfico, esse array serve como o eixo X (horizontal), representando as "datas".

plt.plot(datas,preços[:,0]) # Cria um grafico puxando todas as linhas e puxando a coluna 0 referente aos preços na cidade de Moscou.
plt.show() # Mostra o grafico


Moscow = preços[:,0]
Kaliningrad = preços[:,1]
Petersburg = preços[:,2]   # Separa os preços de cada cidade. (Não estao sendo mostrados no grafico!)
Krasnoda = preços[:,3]
Ekaterinburg = preços[:,4]