import requests
import pandas as pd
from sqlalchemy import create_engine

lista_ceps = ['01153000', '20050000', '70714020']
listas_enderecos = []

for cep in lista_ceps:

    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    req = requests.get(url, timeout=3)
    endereco = req.json()
    listas_enderecos.append([endereco["cep"], endereco["logradouro"], endereco["uf"]])


df_enderecos = pd.DataFrame(listas_enderecos, columns=["cep", "logradouro", "uf"])

db_connection =  'mysql+pymysql://root:123456@localhost:3306/teste'
db_connection = create_engine(db_connection)
df_enderecos.to_sql(con=db_connection, name="enderecos", if_exists= "append", index=False)


print(df_enderecos)