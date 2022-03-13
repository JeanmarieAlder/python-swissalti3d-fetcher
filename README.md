# Python Swissalti3D Fetcher
Simple script to download a list of files from Swissalti3D website.

## How to use
- Make sure to adapt the script to make filepaths and urls match (automation will be added later).
- Go to Swissalti3D website and select the area you want to download.
- Download the .csv file containing the list of all urls to download.
- Place the .csv file in the input folder and adapt the filename in the main.py script
- In a virtual environment (see below), run the script using 'python main.py'

## Create virtual environment
A virtual environment encapsulates all librairies in a separated environment, which does not affect system installed python libraries.
- At the root folder of the project, run 'python -m venv venv'
- This step only has to be done once. If your virtual environment fails, try deleting the whole venv/ folder and recreate it.

## Use virtual environment
If the virtual environment is allready created, you can enter it by using specific command for your OS (see "how to enter python virtual environment on [...])

## Install needed dependencies
Only run this command inside a virtual environment to not affect your entire system python environment.
- 'pip install -r requirements.txt'