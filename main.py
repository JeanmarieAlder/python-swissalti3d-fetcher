
from os.path import basename
import pandas as pd
from shutil import copyfileobj
from time import sleep
from urllib import request

from util import file_allready_dl

print("Welcome to the swissalti3d fetcher!")

df_urls = pd.read_csv("input/Aargau/ch.swisstopo.swissalti3d-vwVOmPEd.csv", header=None)
out_folder = "output/Aargau/"


total_files = len(df_urls)
current_file = 0

print(total_files)

for url in df_urls[0]:
    current_file += 1
    if not file_allready_dl(url):
        filename = basename(url)
        # Download the file from `url` and save it locally under `file_name`:
        with request.urlopen(url) as response, open(out_folder + filename, 'wb') as out_file:
            copyfileobj(response, out_file)
        with open("input/done.csv", "a", encoding="utf-8") as done_file:
            done_file.write(url + '\n')
        print(f"Total files downloaded: {current_file}/{total_files}. {filename}")
        sleep(3)
