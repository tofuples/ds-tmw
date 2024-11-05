# %%
import pandas as pd

# %%

data = {
    "nome": ["julia", "rubens", "hannah", "thays"],
    "sobrenome": ["barbosa", "andrade", "magnani", "ribeiro"],
    "idade": [25, 28, 30, 27]
}
# %%

data["idade"][0]
# %%

df = pd.DataFrame(data)
# %%
df
# %%
df["idade"].iloc[0]
# %%

df["sobrenome"].iloc[2] #dataframe é um conjunto de séries
# %%
#acessar uma linha
df.iloc[0]
# %%

df.index
df.columns
# %%

df.info(memory_usage='deep')
# %%

df.describe()
# %%

df['peso'] = [30, 40, 50, 44] #adicionando coluna nova
# %%
sumario = df.describe()
# %%

sumario['peso']['mean']
# %%

df.head() #mostra os 5 primeiros
df.tail() #mostra as 5 ultimas
# %%
