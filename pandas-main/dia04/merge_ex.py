# %%
import pandas as pd 
# %%
df_customers = pd.read_csv("../data/customers.csv", sep=';')
df_customers
# %%

df_transactions = pd.read_excel("../data/transactions.xlsx")
df_transactions
# %%

df_customers_transactions = df_transactions.merge(df_customers,
                                            how='inner',
                                            left_on=['IdCustomer'],
                                            right_on=['UUID'],
                                            suffixes=["_transação", "_clientes"]
                                            )
# %%

df_transactions_products = pd.read_parquet("../data/transactions_cart.parquet")
df_transactions_products
# %%

df_customers_transactions.merge(df_transactions_products,
                                how='inner',
                                left_on='UUID_transação',
                                right_on='IdTransaction')
# %%

#fazendo os dois merges ao mesmo tempo:
df_join = (df_transactions.merge(df_customer,
                                how="inner",
                                left_on="IdCustomer",
                                right_on="UUID",
                                suffixes=["_transacao", "_cliente"])
                          .merge(df_transactions_product,
                                 how='inner',
                                 left_on="UUID_transacao",
                                 right_on="IdTransaction")
                                 )

df_join
