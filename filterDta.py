import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine('mysql+pymysql://root:@localhost/ocpdb')


query = "SELECT * FROM agents"  
df = pd.read_sql(query, con=engine)


specific_city = 'kh'
filtered_df = df[(df['ville'] == specific_city) & (df['isretired'] == 'non')]


output_file = r'C:\Users\PC\Desktop\FilterData.xlsx'
filtered_df.to_excel(output_file, index=False)

print("Données filtrées exportées avec succès vers le fichier Excel.")
