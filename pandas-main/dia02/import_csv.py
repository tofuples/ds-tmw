# %%
import pandas as pd
# %%
df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers
# %%
df_customers.shape
# %%
df_customers.info(memory_usage='deep')
# %%
df_customers["Points"].describe()
# %%
condicao = df_customers["Points"] > 1000
df_customers[condicao]
# %%
condicao =  df_customers["Points"] == df_customers["Points"].max()
df_customers[condicao]["Name"].iloc[0]
# %%
condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000) 
df_1000_2000 = df_customers[condicao].copy()

df_1000_2000["Points"] = df_1000_2000["Points"] + 1000
df_1000_2000
# %%
df_customers[["Points"]]
# %%
df_customers[["UUID", "Name"]]

# %%
colunas = df_customers.columns.tolist() #converte pra lista
colunas.sort() #ordena
df_customers[colunas]
# %%

df_customers.rename(columns={"Name":"Nome",
                            "Points":"Pontos"})  #dataframe novo
# %%
df_customers.rename(columns={"UUID":"ID"}, inplace=True) #modifica no df_customers
# %%
df_customers
# %%
