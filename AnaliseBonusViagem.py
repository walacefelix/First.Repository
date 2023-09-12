import pandas as pd
from twilio.rest import Client

account_sid = "AC142f589ec162d7de706ea4c803b81138"
auth_token = "8f1278ea60dcba6a17688c778377ff13"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if  (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}')
        message = client.messages.create(
            to="MEU TELEFONE",
            from_="+15077057815",
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}')
        print(message.sid)


