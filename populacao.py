import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Dados.csv')

# Medidas da População:

media_altura = df['Altura'].mean()
media_peso = df['Peso'].mean()
media_idade = df['Idade'].mean()
media_imc = df['Imc'].mean()


mediana_altura = df['Altura'].median()
mediana_peso = df['Peso'].median()
mediana_idade = df['Idade'].median()
mediana_imc = df['Imc'].median()

moda_altura = df['Altura'].mode()
moda_peso = df['Peso'].mode()
moda_idade = df['Idade'].mode()
moda_imc = df['Imc'].mode()

variacao_altura = df['Altura'].var()
variacao_peso = df['Peso'].var()
variacao_idade = df['Idade'].var()
variacao_imc = df['Imc'].var()

desvio_padrao_altura = df['Altura'].std()
desvio_padrao_peso = df['Peso'].std()
desvio_padrao_idade = df['Idade'].std()
desvio_padrao_imc = df['Imc'].std()

coeficiente_variacao_altura = desvio_padrao_altura / media_altura * 100
coeficiente_variacao_peso = desvio_padrao_peso / media_peso * 100
coeficiente_variacao_idade = desvio_padrao_idade / media_idade * 100
coeficiente_variacao_imc = desvio_padrao_imc / media_imc * 100


print(f'Média da altura: {media_altura:.2f}')
print(f'Média do peso: {media_peso:.2f}')
print(f'Média da idade: {media_idade:.2f}')
print(f'Média do IMC: {media_imc:.2f}')

print(f'Mediana da altura:  {mediana_altura}')
print(f'Mediana do peso: {mediana_peso}')
print(f'Mediana da idade:  {mediana_idade}')
print(f'Mediana do IMC:  {mediana_imc}')

# print(f'Moda da altura: {moda_altura::.2f}')
# print(f'Moda do peso: {moda_peso:.2f}')
# print(f'Moda da idade: ', moda_idade)
# print(f'Moda do IMC: ', moda_imc)

# Moda vem como um Series no pandas(pois pode ter mais de uma moda). Tem que passar para list
print(f'Moda da altura: {moda_altura.tolist()}')
print(f'Moda da peso: {moda_peso.tolist()}')
print(f'Moda da idade: {moda_idade.tolist()}')
print(f'Moda da IMC: {moda_imc.tolist()}')

print(f'Variância da altura: {variacao_altura:.4f}')
print(f'Variância do peso: {variacao_peso:.4f}')
print(f'Variância da idade: {variacao_idade:.4f}')
print(f'Variância do IMC: {variacao_imc:.4f}')


print(f'Desvio padrão da altura: {desvio_padrao_altura:.4f}')
print(f'Desvio padrão do peso: {desvio_padrao_peso:.4f}')
print(f'Desvio padrão da idade: {desvio_padrao_idade:.4f}')
print(f'Desvio padrão do IMC: {desvio_padrao_imc:.4f}')

print(f'Coeficiente de variação da altura: {coeficiente_variacao_altura:.4f}')
print(f'Coeficiente de variação do peso: {coeficiente_variacao_peso:.4f}')
print(f'Coeficiente de variação da idade: {coeficiente_variacao_idade:.4f}')
print(f'Coeficiente de variação do IMC: {coeficiente_variacao_imc:.4f}')

# graficos boxplot
plt.figure(1)
boxplot1 = df.boxplot(column=['Altura'])
plt.title("Box plot População")

plt.figure(2)
boxplot2 = df.boxplot(column=['Peso'])
plt.title("Box plot População")

plt.figure(3)
boxplot3 = df.boxplot(column=['Idade'])
plt.title("Box plot População")

plt.figure(4)
boxplot4 = df.boxplot(column=['Imc'])
plt.title("Box plot População")

plt.show()

# graficos dispersao
plt.figure(1)
dispersao1 = df.plot.scatter(x='Altura', y='Peso')
plt.title("Dispersão População")

plt.figure(2)
dispersao2 = df.plot.scatter(x='Altura', y='Idade')
plt.title("Dispersão População")

plt.figure(3)
dispersao3 = df.plot.scatter(x='Altura', y='Imc')
plt.title("Dispersão População")

plt.figure(4)
dispersao4 = df.plot.scatter(x='Peso', y='Idade')
plt.title("Dispersão População")

plt.figure(5)
dispersao5 = df.plot.scatter(x='Peso', y='Imc')
plt.title("Dispersão População")

plt.figure(6)
dispersao6 = df.plot.scatter(x='Idade', y='Imc')
plt.title("Dispersão População")

plt.show()
