import typer
import os
import requests
from utils import validateURL, UrlStatus
from rich import print
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def main(target_url: Annotated[str, typer.Argument()], wordlist_path: Annotated[str, typer.Argument()]):
    print("Welcome to peek v0.1")

    # Checking if target url is a valid url and is reachable and if the wordlist exists
    match validateURL(target_url):
        case UrlStatus.UNREACHABLE:
            print('The target %s appears to be unreachable.', target_url)
        case UrlStatus.BADLY_FORMED:
            print('The target %s appears to be a badly formed URL.', target_url)
        case UrlStatus.UP:
            print('The target %s appears to be up!', target_url)
            if os.path.exists(wordlist_path):
                dirRecon(target_url, wordlist_path)
            else:
                print('Wordlist file "%s" does not exist.', wordlist_path)
    
def dirRecon(target_url: str, wordlist_path: str):       
    print('Starting direcotory recon')
    
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