#Importar Libs
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Chamando datasets
df = pd.read_csv("C:/AmbienteDesenvolvimento/DataPortfolio/Cities_of_Brazil.csv")
df.info()

#Contagem de valores que tem nas colunas
for col in ["cd_uf", "regiao_uf", "bl_capital"]:
    print(df[col].value_counts(), "\n")

#Contagem de quantidade de valores que tem de capital por região
print(df[df["bl_capital"] == True]["regiao_uf"].value_counts())

# Contagem de cidades por estado
counts_estado = df["cd_uf"].value_counts().reset_index()
counts_estado.columns = ["cd_uf", "qtde_cidades"]

#Grafico de nº de cidades por estado
plt.figure(figsize=(10,6))
sns.boxplot(x="qtde_cidades", y="cd_uf", data=counts_estado)
plt.title("Distribuição do Número de Cidades por Estado")
plt.xlabel("Número de Cidades")
plt.ylabel("Estado (UF)")
plt.show()
















