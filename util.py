
import pandas as pd

df_urls_done = pd.read_csv("input/done.csv", header=None)


def file_allready_dl(url):
    for url_done in df_urls_done[0]:
        if url_done == url:
            print(f"File {url} already downloaded, skipping.")
            return True
    return False