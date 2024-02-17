import pandas as pd

def ReadSheet(URL:str, header:int=0):
    data=URL.split('/')
    index=data.index('d')+1
    id=data[index]
    gid=""
    if 'gid=' in URL:
        gid='&gid='+URL.split('gid=')[1]
    URL=f'https://docs.google.com/spreadsheets/d/{id}/export?format=xlsx{gid}'
    return pd.read_excel(URL,header=header)