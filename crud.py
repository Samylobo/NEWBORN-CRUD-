import pandas as pd
from supabase_py import create_client

supabase_url ='https://vawblprycvvjzzykvqnc.supabase.co'
supabase_key ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZhd2JscHJ5Y3Z2anp6eWt2cW5jIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM1NjQ4MTcsImV4cCI6MjAyOTE0MDgxN30.9TPVXzJKW1q3DziLlXc7j5ps71Gd6m0fPVYo2-foJr0'

client = create_client(supabase_url, supabase_key)

#  Obter a lista de tabelas
response = client.table('aluno').select('*').execute()
print(response)

#Crud inserindo dados 
response_insert = client.table('aluno').insert([ {'nome': 'GENERATION', 'sexo': 'F', 'idade': 10}]).execute()
print("deu certo!")
print(response_insert)

# Atualizar o que inserimos 
# Atualizar o que inserimos 
response_update = client.table('aluno').update({'idade': 20}).eq('nome', 'GENERATION').eq('sexo', 'F').execute()
print("\nAtualização realizada:")
print(response_update)

# Deletar o registro inserido
response_delete = client.table('aluno').delete().eq('nome', 'GENERATION').eq('sexo', 'F').eq('idade', 20).execute()
print("\nRegistro excluído:")
print(response_delete)