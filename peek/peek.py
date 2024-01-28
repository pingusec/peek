import typer
import os
import requests
from utils import validateURL, getScriptLocation
from rich import print
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def main(target_url: Annotated[str, typer.Argument()], wordlist_path: Annotated[str, typer.Argument()]):
    print("Welcome to peek v0.1")

    # Checking if target url is a valid url and is reachable
    if validateURL(target_url):
        try:
            response = requests.head(target_url, timeout=1)

        except Exception as err:
            print('Target does not appear to be up.')
        
        else:
            if response.status_code == 200:
                print('Target website up!')
    else:
        print('URL seems to be badly formed!')
    
    # Accessing wordlist   
    
    if os.path.exists(wordlist_path):
        print('Starting directory recon')

        wordlist = open(wordlist_path, 'r')
        for word in wordlist:
            c_url = target_url + '/' + word
            print(c_url.strip())
            response = requests.head(c_url.strip(), allow_redirects=True, timeout=5)
            print(response.status_code)
            if response.status_code != 404:
                print('/' + word + ': EXISTS')

    else:
        print("File does not exist!")

if __name__ == "__main__":
    app()