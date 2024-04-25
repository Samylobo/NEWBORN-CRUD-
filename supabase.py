from supabase_py import create_client

supabase_url ='https://vawblprycvvjzzykvqnc.supabase.co'
supabase_key ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZhd2JscHJ5Y3Z2anp6eWt2cW5jIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM1NjQ4MTcsImV4cCI6MjAyOTE0MDgxN30.9TPVXzJKW1q3DziLlXc7j5ps71Gd6m0fPVYo2-foJr0'
client = create_client(supabase_url, supabase_key)
response = client.select('aluno', 'notas', 'professor').execute()
data = response['data']
