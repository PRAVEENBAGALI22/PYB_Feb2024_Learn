import pandas as pd

df = pd.read_csv(r"C:\Users\pyb\Downloads\smartphone_new.csv")

#print(df)
#print(df.duplicated())
#print(df.info())
#print(df.dtypes)
#print(df.isnull)
#print(df.notnull)
print(df['price'].isnull)
print(df['refresh_rate'].isnull)