# %%
import pandas as pd
# %%

idades = [30, 42, 90, 34]
idades
# %%

#média
media = sum(idades) / len(idades)


#desvio padrão
total = 0
for i in idades:
    total += (media - i)**2
    
variancia = total / (len(idades) -1)
variancia
# %%

series_idades = pd.Series(idades)
series_idades
# %%
# Métodos da séries pandas
# Média
series_idades.mean()

# Variância
series_idades.var()

# Desvio padrão
series_idades.std()

# Mediana
series_idades.median()

# 3o Quartil
series_idades.quantile(0.75)


series_idades.describe()
# %%

series_idades.shape #tuple
# %%

# Alterando index da série
series_idades.index = ['t', 'e', 'o', 'c']
series_idades
# %%

series_idades.loc['t'] #procura pelo índice, .loc[]
# %%

series_idades.iloc[0] #procura pela posição
series_idades.iloc[0:2]
# %%

series_idades.name = 'idades'
series_idades = pd.Series(idades, name="idades")
# %%
