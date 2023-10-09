from dataAnalysis import AnalysisGraphics

# Dicionário de dados
# Dados de cada pessoa: nome, sexo, idade, cidade, estado e estado civil
people = [
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
    {'Nome': 'Beatriz', 'Sexo': 'Feminino', 'Idade': 37, 'Cidade': 'Campo Grande', 'Estado': 'MS', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Beatriz', 'Sexo': 'Feminino', 'Idade': 37, 'Cidade': 'Campo Grande', 'Estado': 'MS', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Beatriz', 'Sexo': 'Feminino', 'Idade': 37, 'Cidade': 'Campo Grande', 'Estado': 'MS', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Beatriz', 'Sexo': 'Feminino', 'Idade': 37, 'Cidade': 'Campo Grande', 'Estado': 'MS', 'Estado Civil': 'Casado(a)'},
    {'Nome': 'Beatriz', 'Sexo': 'Feminino', 'Idade': 37, 'Cidade': 'Campo Grande', 'Estado': 'MS', 'Estado Civil': 'Casado(a)'}]

# AnalysisGraphics(people).genreNumber()
# AnalysisGraphics(people).numberPerAge()
# AnalysisGraphics(people).numberPerGroupAge()
# AnalysisGraphics(people).numberPerState()
# AnalysisGraphics(people).numberPerCivilState()
# AnalysisGraphics(people).numberPerCity()