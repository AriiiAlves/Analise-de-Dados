# projeto 1: ler um dicionário com vários dados de uma pessoa, e fazer gráficos de estatísticas com múltiplos desses dados,
# que são todos salvos em um único arquivo pdf como relatório

# estatísticas:
#   quantidade de M e F,
#   média de idades,
#   quantidade de pessoas jovens, adultas e idosas,
#   quantidade de pessoas por estado,
#   quantidade de pessoas por estado civil,
#   número de pessoas por cidade

# Dados da pessoa: nome, sexo, idade, cidade, estado, estado civil

import pandas as pd
import matplotlib.pyplot as plt

temp1, temp2, temp3, temp4 = 0, 0, 0, 0
dicionario, var1, var2 = {}, {}, {}
labels, lista = [], []

# Dicionário de dados
pessoas = [
    {'Nome': 'João', 'Sexo': 'Masculino', 'Idade': 45, 'Cidade': 'Recife', 'Estado': 'PE', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Maria', 'Sexo': 'Feminino', 'Idade': 52, 'Cidade': 'Fortaleza', 'Estado': 'CE', 'Estado Civil': 'Solteiro(a)'},
    {'Nome': 'José', 'Sexo': 'Masculino', 'Idade': 27, 'Cidade': 'Belo Horizonte', 'Estado': 'MG', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Ana', 'Sexo': 'Feminino', 'Idade': 45, 'Cidade': 'São Paulo', 'Estado': 'SP', 'Estado Civil': 'Divorciado(a)'},
    {'Nome': 'Carlos', 'Sexo': 'Masculino', 'Idade': 32, 'Cidade': 'Goiânia', 'Estado': 'GO', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Mariana', 'Sexo': 'Feminino', 'Idade': 34, 'Cidade': 'Rio de Janeiro', 'Estado': 'RJ', 'Estado Civil': 'Solteiro(a)'},
    {'Nome': 'Pedro', 'Sexo': 'Masculino', 'Idade': 60, 'Cidade': 'São Luís', 'Estado': 'MA', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Camila', 'Sexo': 'Feminino', 'Idade': 22, 'Cidade': 'Brasília', 'Estado': 'DF', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Luiz', 'Sexo': 'Masculino', 'Idade': 34, 'Cidade': 'Campo Grande', 'Estado': 'MS', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Amanda', 'Sexo': 'Feminino', 'Idade': 59, 'Cidade': 'Manaus', 'Estado': 'AM', 'Estado Civil': 'Viúvo(a)'},
    {'Nome': 'Paulo', 'Sexo': 'Masculino', 'Idade': 24, 'Cidade': 'Salvador', 'Estado': 'BA', 'Estado Civil': 'Solteiro(a)'},
    {'Nome': 'Isabela', 'Sexo': 'Feminino', 'Idade': 53, 'Cidade': 'Palmas', 'Estado': 'TO', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Fernando', 'Sexo': 'Masculino', 'Idade': 35, 'Cidade': 'Recife', 'Estado': 'PE', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Laura', 'Sexo': 'Feminino', 'Idade': 25, 'Cidade': 'Aracaju', 'Estado': 'SE', 'Estado Civil': 'Solteiro(a)'},
    {'Nome': 'Rafael', 'Sexo': 'Masculino', 'Idade': 48, 'Cidade': 'Natal', 'Estado': 'RN', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Juliana', 'Sexo': 'Feminino', 'Idade': 46, 'Cidade': 'Goiânia', 'Estado': 'GO', 'Estado Civil': 'Divorciado(a)'},
    {'Nome': 'Gustavo', 'Sexo': 'Masculino', 'Idade': 25, 'Cidade': 'Cuiabá', 'Estado': 'MT', 'Estado Civil': 'Solteiro(a)'},
    {'Nome': 'Natália', 'Sexo': 'Feminino', 'Idade': 49, 'Cidade': 'Florianópolis', 'Estado': 'SC', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Marcos', 'Sexo': 'Masculino', 'Idade': 57, 'Cidade': 'Recife', 'Estado': 'PE', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Thais', 'Sexo': 'Feminino', 'Idade': 38, 'Cidade': 'São Paulo', 'Estado': 'SP', 'Estado Civil': 'Solteiro(a)'},
    {'Nome': 'Ricardo', 'Sexo': 'Masculino', 'Idade': 42, 'Cidade': 'Belo Horizonte', 'Estado': 'MG', 'Estado Civil': 'Solteiro(a)'},
    {'Nome': 'Carolina', 'Sexo': 'Feminino', 'Idade': 47, 'Cidade': 'Rio de Janeiro', 'Estado': 'RJ', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Bruno', 'Sexo': 'Masculino', 'Idade': 51, 'Cidade': 'São Paulo', 'Estado': 'SP', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Patrícia', 'Sexo': 'Feminino', 'Idade': 41, 'Cidade': 'Recife', 'Estado': 'PE', 'Estado Civil': 'Divorciado(a)'},
    {'Nome': 'Eduardo', 'Sexo': 'Masculino', 'Idade': 33, 'Cidade': 'Porto Alegre', 'Estado': 'RS', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Luisa', 'Sexo': 'Feminino', 'Idade': 36, 'Cidade': 'Salvador', 'Estado': 'BA', 'Estado Civil': 'Solteiro(a)'},
    {'Nome': 'Henrique', 'Sexo': 'Masculino', 'Idade': 29, 'Cidade': 'Goiânia', 'Estado': 'GO', 'Estado Civil': 'Solteiro(a)'},
    {'Nome': 'Luana', 'Sexo': 'Feminino', 'Idade': 55, 'Cidade': 'São Luís', 'Estado': 'MA', 'Estado Civil': 'Viúvo(a)'},
    {'Nome': 'Felipe', 'Sexo': 'Masculino', 'Idade': 23, 'Cidade': 'Brasília', 'Estado': 'DF', 'Estado Civil': 'Solteiro(a)'},
    {'Nome': 'Beatriz', 'Sexo': 'Feminino', 'Idade': 37, 'Cidade': 'Campo Grande', 'Estado': 'MS', 'Estado Civil': 'Casado(a)'}]


pessoas_df = pd.DataFrame(pessoas)

## Total de homens e total de mulheres ##

for i in range(0, pessoas_df.shape[0]):
    if pessoas_df.loc[i, 'Sexo'] == 'Masculino':
        temp1 += 1
    elif pessoas_df.loc[i, 'Sexo'] == 'Feminino':
        temp2 += 1

# Gerando gráfico

labels = ['Masculino', 'Feminino']
var1 = [temp1, temp2]

# fig: manipula figura
# ax: manipula gráfico

fig, ax = plt.subplots(figsize=(5, 5))
ax.bar(labels, var1, color=['#3489eb', '#eb4034'])
plt.axis(ymax = max(var1) + 1)
ax.set_title('Quantidade de pessoas por gênero')
ax.set_ylabel("Quantidade")
ax.set_xlabel('Gênero')
plt.show()

temp1, temp2 = 0, 0
labels.clear()

## Média de idades e quantidade por idade ## (falta fazer alguma coisa com isso aqui)
for i in range(0, pessoas_df.shape[0]):
    temp1 += pessoas_df.loc[i, 'Idade']
temp1 /= pessoas_df.shape[0]

# print(f"Idade média: {round(temp1)}")

temp1 = 0

## Quantidade de pessoas por idade ##
for i in range(0, pessoas_df.shape[0]):
    if pessoas_df.loc[i, 'Idade'] not in lista:
        lista.append(pessoas_df.loc[i, 'Idade'])
lista.sort()

for i in lista:
    dicionario[i] = 0
lista.clear()

for i in range(0, pessoas_df.shape[0]):
    dicionario[pessoas_df.loc[i, 'Idade']] += 1

# Gerando gráfico

for i in dicionario:
    labels.append(i)
for i in dicionario:
    lista.append(dicionario[i])

# fig: manipula figura
# ax: manipula gráfico

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(labels, lista)
plt.xticks(range(min(labels), max(labels) + 1))
plt.yticks(range(min(lista), max(lista) + 1))
ax.set_title('Quantidade de pessoas por idade')
ax.set_xlabel('Idade')
ax.set_ylabel("Número de pessoas")
plt.show()

temp1 = 0
labels.clear()
lista.clear()
dicionario.clear()

## Quantidade de idades por grupos ##
for i in range(0, pessoas_df.shape[0]):
    if pessoas_df.loc[i, 'Idade'] >= 0 and pessoas_df.loc[i, 'Idade'] < 20:
        temp1 += 1
    elif pessoas_df.loc[i, 'Idade'] >= 20 and pessoas_df.loc[i, 'Idade'] < 60:
        temp2 += 1
    elif pessoas_df.loc[i, 'Idade'] >= 60:
        temp3 += 1

# Gerando gráfico

labels = ['Jovens', 'Adultos', 'Idosos']
lista = [temp1, temp2, temp3]

# fig: manipula figura
# ax: manipula gráfico

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(labels, lista)
plt.axis(ymax = max(lista) + 10)
ax.set_title('Quantidade de pessoas por faixa etária')
ax.set_xlabel('Faixa etária')
ax.set_ylabel("Número de pessoas")
plt.show()

temp1, temp2, temp3 = 0, 0, 0
labels.clear()
lista.clear()

## Quantidade de pessoas por estado ##
for i in range(0, pessoas_df.shape[0]):
    if pessoas_df.loc[i, 'Estado'] not in dicionario.keys():
        for j in range(0, pessoas_df.shape[0]):
            if pessoas_df.loc[j, 'Estado'] == pessoas_df.loc[i, 'Estado']:
                temp1 += 1
        dicionario[f"{pessoas_df.loc[i, 'Estado']}"] = temp1
        temp1 = 0

# Gerando gráfico

for i in dicionario:
    labels.append(i)
    lista.append(dicionario[i])

# fig: manipula figura
# ax: manipula gráfico

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(labels, lista)
plt.axis(ymax = max(lista) + 1)
ax.set_title('Quantidade de pessoas por estado')
ax.set_xlabel('Estado')
ax.set_ylabel("Número de pessoas")
plt.show()

temp1 = 0
dicionario.clear()
labels.clear()
lista.clear()

## Quantidade de pessoas por estado civil ##
for i in range(0, pessoas_df.shape[0]):
    if pessoas_df.loc[i, 'Estado Civil'] == 'Solteiro(a)':
        temp1 += 1
    elif pessoas_df.loc[i, 'Estado Civil'] == 'Casado(a)':
        temp2 += 1
    elif pessoas_df.loc[i, 'Estado Civil'] == 'Divorciado(a)':
        temp3 += 1
    elif pessoas_df.loc[i, 'Estado Civil'] == 'Viúvo(a)':
        temp4 += 1

# Gerando gráfico

labels = ['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo']
lista = [temp1, temp2, temp3, temp4]

# fig: manipula figura
# ax: manipula gráfico

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(labels, lista)
plt.axis(ymax = max(lista) + 1)
ax.set_title('Quantidade de pessoas por estado civil')
ax.set_xlabel('Estado civil')
ax.set_ylabel("Número de pessoas")
plt.show()

temp1, temp2, temp3, temp4 = 0, 0, 0, 0
labels.clear()
lista.clear()

## Número de pessoas por cidade ##
for i in range(0, pessoas_df.shape[0]):
    if pessoas_df.loc[i, 'Cidade'] not in dicionario.keys():
        for j in range(0, pessoas_df.shape[0]):
            if pessoas_df.loc[j, 'Cidade'] == pessoas_df.loc[i, 'Cidade']:
                temp1 += 1
        dicionario[f"{pessoas_df.loc[i, 'Cidade']}"] = temp1
        temp1 = 0

# Gerando gráfico

for i in dicionario:
    labels.append(i)
    lista.append(dicionario[i])

# fig: manipula figura
# ax: manipula gráfico

fig, ax = plt.subplots(figsize=(5, 10))
ax.barh(labels, lista, lw = 5)
plt.axis(xmax = max(lista) + 1)
ax.set_title('Quantidade de pessoas por cidade')
ax.set_xlabel('Número de pessoas')
ax.set_ylabel("Cidade")
plt.show()

temp1 = 0
dicionario.clear()
labels.clear()
lista.clear()