# %%
import pandas as pd

# %%

df = pd.read_csv("../data/customers.csv", sep=";")
df["Points"]
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
