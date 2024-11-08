# %%
import pandas as pd
import numpy as np

data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan],
}

df = pd.DataFrame(data)
df
# %%
df["idade"].isna().sum() #soma todos que não são número

#na = dado faltante

# %%
df.isna()

# %%

df.isna().sum()

# %%
df.isna().mean() #proporção

# %%
#df.fillna(0) preenche os dados faltans com 0
df.fillna({
        "idade": df["idade"].mean(),
        "renda":df["renda"].mean(),
        }) #preenche com as médias

# %%
df.dropna() #remove qualquer linha que tem NaN
# %%
df.dropna(subset=["idade", "renda"], how='all') #remove se em ambas colunas for NaN
df.dropna(subset=["idade", "renda"], how='any') #remove se em pelo menos uma coluna for NaN

#%%
df.dropna(axis=1) #deleta as colunas com NaN

# %%
df.dropna(axis=1, thresh=3)