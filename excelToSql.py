import pandas as pd
from sqlalchemy import create_engine

agents_file = r'C:\Users\PC\Desktop\Agents.xlsx'
demandes_file = r'C:\Users\PC\Desktop\demandes.xlsx'


df = pd.read_excel(agents_file)
df2 = pd.read_excel(demandes_file)


engine = create_engine('mysql+pymysql://root:@localhost/ocpdb')

df.to_sql('agents', con=engine, if_exists='replace', index=False)
df2.to_sql('demandes', con=engine, if_exists='replace', index=False)

print("Données insérées avec succès dans la base de données.")
