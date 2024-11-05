# %%
import pandas as pd 

# %%
dados = {
    "Nome": ["Gabriel", "Theo", "Julia"],
    "idade": [31, 31, 14]
}
# %%
df = pd.DataFrame(dados)
# %%
df
# %%
sumario = df.describe()
sumario
# %%
sumario['idade'].mean()
# %%
df['Nome'].tail(1)

# %%
