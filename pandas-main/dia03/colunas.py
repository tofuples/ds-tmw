# %%
import pandas as pd
import numpy as np

#criando novas colunas e fazendo operações, função lambda
# %%
df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%
#criando coluna nova
df["Points_double"] = df["Points"] * 2
df
# %%
df["Points_ratio"] = df["Points_double"] / df["Points"]
df
# %%

df["Constante"] = 1
df
# %%
df["Raiz"] = np.sqrt(df["Points_double"])
df["Log"] = np.log(df["Points_ratio"])
df
# %%
np.log(df[["Points", "Points_double"]])

# %%
nomes_caps = []
for i in df["Name"]:
    nomes_caps.append(i.upper())
    
df["Nomes2"] = nomes_caps
df
# %%
#nomes em caps sem usar for
df["Name"] = df["Name"].str.upper()
df
# %%
#pegando apenas o que vem antes de "_" nos nomes
def get_first(x:str):
    return x.split("_")[0]

df["Name_first"] = df["Name"].apply(get_first)
df
# %%
#lambda
# soma = lambda x,y: x+y
# get_f = lambda nome: nome.split("_")[0]
# get_f("Julia_Elisa")

df["Name"].apply(lambda x:x.split("_")[0])

# %%
#intervalo de pontuação
def intervalo_pontos(pontos):
    if pontos < 1000:
        return "baixo"
    if pontos < 2500:
        return "médio"
    else:
        return "alto"
    
df["Faixa_pontos"] = df["Points"].apply(intervalo_pontos)
df
# %%
#pegar apenas os 3 últimos de UUID
df["UUID"].apply(lambda x:x[-3:])

 
 # def tres(uuid):
#     return uuid[-3:]

# df["UUID"].apply(tres)
# %%
