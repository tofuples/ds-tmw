# %% 
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df
# %%
# a ultima transacao de cada IdCostumer
#1) ordenar pelas datas (do mais recente pro mais antigo)
#1) drop_duplicates do Id costumer, deixar só o mais recente (first)

# %%
df_last = (df.sort_values(by="DtTransaction", ascending=False)
        .drop_duplicates(subset="IdCustomer", keep='first'))

df_last["IdCustomer"].nunique() #contas quantos valores únicos
# %%
#filtrar apenas um idcostumer pra ver se bate

condicao = df["IdCustomer"] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df[condicao]
# %%

df_last[df["IdCustomer"] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']
# %%
