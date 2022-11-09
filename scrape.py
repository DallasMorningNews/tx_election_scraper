import requests
import json
import pandas as pd

headers =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
with open('results.txt') as f:
    lines = f.readlines()
start = int(lines[0])
for i in range(start, 500):
    try:
        results = requests.get(f'https://results.texas-election.com/static/data/election/47009/{i}/County.json', headers=headers).json()
    except:
        results = requests.get(f'https://results.texas-election.com/static/data/election/47009/{i-1}/County.json', headers=headers).json()
        with open('results.txt', 'w') as f:
            f.write(str(i))
        break

ds = []
for i in results.keys():
    d = {}
    d['county'] = results[f'{i}']['N'] #County Name
    d['orourke'] = results[f'{i}']['Races']['1004']['C']['331257']['V'] 
    d['abbott'] = results[f'{i}']['Races']['1004']['C']['331306']['V'] 
    ds.append(d)

df = pd.DataFrame(ds)

winning = []
for i in range(0, len(df)):
    if df['orourke'][i] > df['abbott'][i]:
        winning.append('orourke')
    elif df['orourke'][i] == df['abbott'][i]:
        winning.append('tie')
    else:
        winning.append('abbott')

df['winning'] = winning
df.to_csv('tx_election.csv', index=False)