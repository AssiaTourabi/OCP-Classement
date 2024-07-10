import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:@localhost/ocpdb')


query = "SELECT * FROM agents"
df = pd.read_sql(query, con=engine)


output_file = r'C:\Users\PC\Desktop\AgentsData.xlsx'


df.to_excel(output_file, index=False)

print("Données exportées avec succès vers le fichier Excel.")

