# %%
import pandas as pd

# %%

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%

df.sort_values(by=["Points", "Name"], ascending=[False, True]) #ordena pelos pontos e ordena os nomes em ordem alfabética

# %%
df.sort_values(by="Points", ascending=False, inplace=True) #ordena pelos pontos
df.rename(columns={"Name":"Nome",
                   "Points":"Pontos"}, inplace=True)
df
# %%
#sem o inplace
df = (df.sort_values(by="Points", ascending=True)
        .rename(columns={"Name":"Nome", "Points": "Pontos"}))
df
# %%
