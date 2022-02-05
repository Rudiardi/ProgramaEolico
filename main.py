from bz2 import compress
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#importar os dados
turbina = pd.read_csv(r'C:\Users\rudij_cx4b0ag\Documents\PROJETOS\PROGRAMAÇÃO\PYTHON\PROJETO EOLICO\DATA\T1.csv')
#trocar os nomes das colunas
turbina.columns = ['Data/hora','Potência Ativa(Kw)', 'Velocidade do vento(m/s)','Curva teórica(Kwh)','Direção do Vento(°)']
#remover coluna
del turbina['Direção do Vento(°)']
#alterar columa de data e hora
turbina['Data/hora'] = pd.to_datetime(turbina['Data/hora'])
print(turbina)

#plotar gráfico de disperção
sns.scatterplot(data=turbina, x='Velocidade do vento(m/s)',y ='Potência Ativa(Kw)' )
plt.show()
#plotar gráfico da curva teorica
sns.scatterplot(data=turbina, x='Velocidade do vento(m/s)',y ='Curva teórica(Kwh)' )
plt.show()
#definindo os limites aceitaveis
potReal=turbina['Potência Ativa(Kw)'].tolist()
potTeorica=turbina['Curva teórica(Kwh)'].tolist()
potMax = []
potMin = []
#criar um for para atualizar os valores da nova lista com + e - 5%
for potencia in potTeorica:
    #appende reescreve
    potMax.append(potencia*1.05)
    potMin.append(potencia*0.95)

print (len(potMax),len(potMin),len(potTeorica))

#determinar quais pontos então contidos nos limites
dentroLimite = []
for p, potencia in enumerate(potReal):
    if potencia>=potMin[p] and potencia<=potMax[p]:
        dentroLimite.append('Dentro')
    elif potencia == 0:
        dentroLimite.append('Zero')
    else:
        dentroLimite.append('Fora')
#verificar a potentagem de pontos dentro e fora
print(dentroLimite.count('Dentro')/len(dentroLimite))
print(dentroLimite.count('Zero')/len(dentroLimite))
print(dentroLimite.count('Fora')/len(dentroLimite))

#aplicar os limites a uma nova coluna
turbina['Dentro Limite'] = dentroLimite
print(turbina)

#novos gráficos
#plotar gráfico de disperção
cores = {'Dentro':'blue','Fora':'red','Zero':'orange'}
sns.scatterplot(data=turbina, x='Velocidade do vento(m/s)',y ='Potência Ativa(Kw)', hue='Dentro Limite', s=1, palette=cores)
plt.show()
