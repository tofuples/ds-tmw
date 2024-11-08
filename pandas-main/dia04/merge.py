# %%

import pandas as pd

data_users = {
    "id": [1,2,3,4],
    "nome":["Teo", "Mat", "Nah", "Mah"],
    "idade": [31,31,32,32]
}

df_user = pd.DataFrame(data_users)
df_user

# %%

data_transacoes = {
    "id_user": [1,1,1,2,3,3,5],
    "valor":[432,532,123,6,4,87,10],
    "qtProdutos": [2,1,3,6,10,2,7]
}

df_transacao = pd.DataFrame(data_transacoes)
df_transacao

# %%

df_transacao.merge(df_user)
# %%

df_transacao.merge(df_user,
                   how='left', #manter os dados da esquerda(df_transcao) fixos
                   left_on=['id_user'], #quais são equivalentes entre o left e right
                   right_on=['id'],                   
                   )

# %%

df_transacao.merge(df_user,
                   how='inner', #intersecção
                   left_on=['id_user'],
                   right_on=['id'],                   
                   )
# %%
df_transacao.merge(df_user,
                   how='right', #df_ser é a referencia
                   left_on=['id_user'],
                   right_on=['id'],                   
                   )
# %%
