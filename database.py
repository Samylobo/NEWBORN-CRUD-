import pandas as pd
from supabase_py import create_client

supabase_url ='https://vawblprycvvjzzykvqnc.supabase.co'
supabase_key ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZhd2JscHJ5Y3Z2anp6eWt2cW5jIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM1NjQ4MTcsImV4cCI6MjAyOTE0MDgxN30.9TPVXzJKW1q3DziLlXc7j5ps71Gd6m0fPVYo2-foJr0'

client = create_client(supabase_url, supabase_key)

#  Obter a lista de tabelas
response = client.table('aluno').select('*').execute()
print(response)
alunos_df = pd.DataFrame(response['data'])

response_notas = client.table('notas').select("id_aluno", "nota").execute()
notas_df = pd.DataFrame(response_notas['data'])
print(notas_df)
# mesclando as tabelas dos alunos e notas
aluno_notas_df = pd.merge(alunos_df, notas_df, left_on='id_aluno', right_on='id_aluno')
print(aluno_notas_df)
# analisando qual é o melhor aluno 
melhor_aluno = aluno_notas_df.loc[aluno_notas_df['nota'].idxmax()]
print(melhor_aluno)
# o aluno mediano 
notas_medianas = aluno_notas_df['nota'].median()
aluno_mediano = aluno_notas_df.loc[aluno_notas_df['nota']== notas_medianas]
print(aluno_mediano)
# o pior aluno 
pior_aluno = aluno_notas_df.loc[aluno_notas_df['nota'].idxmin()]
print(pior_aluno)


 




