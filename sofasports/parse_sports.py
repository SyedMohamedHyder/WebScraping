import json
import pandas as pd

with open('sports.json', 'r') as file:
    sports = json.load(file)

df = pd.json_normalize(sports['standings'][1]['rows'])
df.to_csv('sports.csv', index=False)