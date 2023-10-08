import pandas as pd
import matplotlib.pyplot as plt

class AnalysisGraphics:
    def __init__(self, datadict):
        self.people_df = pd.DataFrame(datadict)

    # Gráfico do número de pessoas por gênero
    def genreNumber(self):
        labels, data = [], []
        temp1, temp2 = 0, 0
        
        # Gerando dados estatísticos
        for i in range(0, self.people_df.shape[0]):
            if self.people_df.loc[i, 'Sexo'] == 'Masculino':
                temp1 += 1
            elif self.people_df.loc[i, 'Sexo'] == 'Feminino':
                temp2 += 1

        # Criando as listas label e data, onde label é a legenda e data são os dados
        labels = ['Masculino', 'Feminino']
        data = [temp1, temp2]

        # Gerando gráfico
        plt.figure()
        plt.bar(labels, data, color=['#3489eb', '#eb4034'])
        plt.yticks(self.setRange(max(data)))
        plt.suptitle('Quantidade de pessoas por gênero')
        plt.ylabel("Quantidade")
        plt.xlabel('Gênero')
        plt.tight_layout()
        plt.savefig('temp/genreNumber.png')
        plt.clf()

    # Função que retorna a idade média de todas as pessoas
    def middleAge(self):
        temp1 = 0

        for i in range(0, self.people_df.shape[0]):
            temp1 += self.people_df.loc[i, 'Idade']
        temp1 /= self.people_df.shape[0]

        # return(temp1)

    # Gráfico do número de pessoas por idade
    def numberPerAge(self):
        labels, data = [], []
        dictionary = {}

        # Gerando dados estatísticos
        for i in range(0, self.people_df.shape[0]):
            if self.people_df.loc[i, 'Idade'] not in data:
                data.append(self.people_df.loc[i, 'Idade'])
        data.sort()

        for i in data:
            dictionary[i] = 0
        data.clear()

        for i in range(0, self.people_df.shape[0]):
            dictionary[self.people_df.loc[i, 'Idade']] += 1

        # Criando as listas label e data, onde label é a legenda e data são os dados
        for i in dictionary:
            labels.append(i)
        for i in dictionary:
            data.append(dictionary[i])

        # Gerando gráfico
        plt.figure(plt.figure(figsize=(15, 10)))
        plt.bar(labels, data)
        plt.xticks(range(min(labels), max(labels) + 1))
        plt.yticks(self.setRange(max(data)))
        plt.suptitle('Quantidade de pessoas por idade')
        plt.xlabel('Idade')
        plt.ylabel("Número de pessoas")
        plt.tight_layout()
        plt.savefig('temp/numberPerAge.png')
        plt.clf()
    
    # Gráfico do número de pessoas por faixa etária
    def numberPerGroupAge(self):
        labels, data = [], []
        temp1, temp2, temp3 = 0, 0, 0

        # Gerando dados estatísticos
        for i in range(0, self.people_df.shape[0]):
            if self.people_df.loc[i, 'Idade'] >= 0 and self.people_df.loc[i, 'Idade'] < 20:
                temp1 += 1
            elif self.people_df.loc[i, 'Idade'] >= 20 and self.people_df.loc[i, 'Idade'] < 60:
                temp2 += 1
            elif self.people_df.loc[i, 'Idade'] >= 60:
                temp3 += 1

        # Criando as listas label e data, onde label é a legenda e data são os dados
        labels = ['Jovens', 'Adultos', 'Idosos']
        data = [temp1, temp2, temp3]

        # Gerando gráfico
        plt.figure()
        plt.bar(labels, data)
        plt.yticks(self.setRange(max(data)))
        plt.suptitle('Quantidade de pessoas por faixa etária')
        plt.xlabel('Faixa etária')
        plt.ylabel("Número de pessoas")
        plt.tight_layout()
        plt.savefig('temp/numberPerGroupAge.png')
        plt.clf()
    
    # Gráfico do número de pessoas por Estado
    def numberPerState(self):
        dictionary = {}
        labels, data = [], []
        temp1 = 0

        # Gerando dados estatísticos
        for i in range(0, self.people_df.shape[0]):
            if self.people_df.loc[i, 'Estado'] not in dictionary.keys():
                for j in range(0, self.people_df.shape[0]):
                    if self.people_df.loc[j, 'Estado'] == self.people_df.loc[i, 'Estado']:
                        temp1 += 1
                dictionary[f"{self.people_df.loc[i, 'Estado']}"] = temp1
                temp1 = 0

        # Criando as listas label e data, onde label é a legenda e data são os dados
        for i in dictionary:
            labels.append(i)
            data.append(dictionary[i])

        # Gerando gráfico
        plt.figure()
        plt.bar(labels, data)
        plt.yticks(self.setRange(max(data)))
        plt.suptitle('Quantidade de pessoas por estado')
        plt.xlabel('Estado')
        plt.ylabel("Número de pessoas")
        plt.tight_layout()
        plt.savefig('temp/numberPerState.png')
        plt.clf()

    # Gráfico do número de pessoas por estado civil
    def numberPerCivilState(self):
        labels, data = [], []
        temp1, temp2, temp3, temp4 = 0, 0, 0, 0

        # Gerando dados estatísticos
        for i in range(0, self.people_df.shape[0]):
            if self.people_df.loc[i, 'Estado Civil'] == 'Solteiro(a)':
                temp1 += 1
            elif self.people_df.loc[i, 'Estado Civil'] == 'Casado(a)':
                temp2 += 1
            elif self.people_df.loc[i, 'Estado Civil'] == 'Divorciado(a)':
                temp3 += 1
            elif self.people_df.loc[i, 'Estado Civil'] == 'Viúvo(a)':
                temp4 += 1

        # Criando as listas label e data, onde label é a legenda e data são os dados
        labels = ['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo']
        data = [temp1, temp2, temp3, temp4]

        # Gerando gráfico
        plt.figure()
        plt.bar(labels, data)
        plt.yticks(self.setRange(max(data)))
        plt.suptitle('Quantidade de pessoas por estado civil')
        plt.xlabel('Estado civil')
        plt.ylabel("Número de pessoas")
        plt.tight_layout()
        plt.savefig('temp/numberPerCivilState.png')
        plt.clf()
    
    # Gráfico do número de pessoas por cidade
    def numberPerCity(self):
        dictionary = {}
        labels, data = [], []
        temp1 = 0

        # Gerando dados estatísticos
        for i in range(0, self.people_df.shape[0]):
            if self.people_df.loc[i, 'Cidade'] not in dictionary.keys():
                for j in range(0, self.people_df.shape[0]):
                    if self.people_df.loc[j, 'Cidade'] == self.people_df.loc[i, 'Cidade']:
                        temp1 += 1
                dictionary[f"{self.people_df.loc[i, 'Cidade']}"] = temp1
                temp1 = 0

        # Criando as listas label e data, onde label é a legenda e data são os dados
        for i in dictionary:
            labels.append(i)
            data.append(dictionary[i])

        # Gerando gráfico
        plt.figure()
        plt.barh(labels, data)
        plt.xticks(self.setRange(max(data)))
        plt.suptitle('Quantidade de pessoas por cidade')
        plt.xlabel('Número de pessoas')
        plt.ylabel("Cidade")
        plt.tight_layout()
        plt.savefig('temp/numberPerCity.png')
        plt.clf()
    
    # Função que cria uma lista com intervalos de números, utilizados para a visualização (ticks) dos dados do gráfico
    def setRange(self, maxvalue):
        set_range = []
        n = maxvalue

        if n > 10:
            op1 = n % 10
            op2 = n - op1

            if op1 == 5 or op1 == 0:
                n += 6
            elif op1 < 5:
                n = op2 + 6
            elif n > 5:
                n = op2 + 11

            for i in range(0, n, 5):
                set_range.append(i)

            return(set_range)
        else:
            for i in range(0, maxvalue + 1):
                set_range.append(i)
            return(set_range)

    ## def GeneratePDF(self):

    ## o pdf vai conter uma tabela com todos os dados, e os gráficos estatísticos gerados