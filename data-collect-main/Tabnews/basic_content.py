# %% 
import requests
# %%

def get_response(**kwargs):
    url = "https://www.tabnews.com.br/api/v1/contents/"
    resp = requests.get(url, params=kwargs)
    return resp



# %%
resp = get_response(page=1, per_page=100, strategy="new")
resp.json()
# %%
