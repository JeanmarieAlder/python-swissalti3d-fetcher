import pandas as pd

df_urls = pd.read_csv("input/Geneve/ch.swisstopo.swissalti3d-V3ZMCdHM.csv", header=None)
df_urls_done = pd.read_csv("input/done.csv", header=None)
i = 0

for url in df_urls[0]:
    if str(df_urls_done[0].any()) == url:
        print(f'{url} found')
        i += 1

print(i)