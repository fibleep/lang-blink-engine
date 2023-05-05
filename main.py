import pandas as pd

df: pd.DataFrame = pd.read_json('db.json')

print(df.info())