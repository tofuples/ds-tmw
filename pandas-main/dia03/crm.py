#rfv/rfm 
import pandas as pd

data = {
    "nome": ["Teo", "Nah", "Maria", "Lara"],
    "recencia": [1,30,10,45],
    "valor":[100,2000, 15, 500],
    "frequencia":[2, 5, 1, 15]
}

df_crm = pd.DataFrame(data)
df_crm
# %%
#criar um parametro para gerar as notas finais

#Se recencia <= 10: 10
#Se recencia >10 e <30 : 5
#Se recencia > 30: 0

#Se valor < 100: 0
#Se valor > 100 e <1000: 5
#Se valor > 1000: 10

#Se frequencia > 10: 10
#Se frequencia > 5 e < 10 : 5
#Se frequencia < 5: 0

#nota_final = soma dos pontos

def rfv(row): #funcao que recebe cada linha do df e acessa as infos de cada indice
    nota = 0
    if row['recencia'] <= 10:
        nota += 10
    elif 10 < row['recencia'] <= 30:
        nota += 5
    else:
        nota += 0
        
    if row['valor'] < 100:
        nota += 0
    elif 100 <= row['valor'] < 1000:
        nota += 5
    else:
        nota += 10
        
    if row['frequencia'] > 10:
        nota += 10
    elif 5 <= row['frequencia'] < 10:
        nota +=5
    else:
        nota += 0
        
    return nota

# %%
df_crm.iloc[0] #o que será passado na função
# %%
df_crm.apply(rfv, axis=1)
#a funcao recebe cada linha inteira e acessa as infos de cada linha
# o axis é pra ele aplicar a função na horizontal, ele te passa as colunas em forma de linhas (iloc[0])
# %%

df_crm["RFV"] = df_crm.apply(rfv, axis=1)
df_crm

# %%
df_crm.sort_values(by=["RFV"], ascending=[False])

# %%
