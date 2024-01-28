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
            print(f'The target {target_url} appears to be unreachable.')
        
        case UrlStatus.BADLY_FORMED:
            print(f'The target {target_url} appears to be a badly formed URL.')
        
        case UrlStatus.UP:
            print(f'The target {target_url} appears to be up!')
        
            if os.path.exists(wordlist_path):
                dirRecon(target_url, wordlist_path)
        
            else:
                print('Wordlist file "%s" does not exist.', wordlist_path)

def dirRecon(target_url: str, wordlist_path: str):
    print('Starting directory recon')

    default_extensions = ['/', '.html', '.htm', '.php', '.js', '.jsx', '.pdf']

    wordlist = open(wordlist_path, 'r')

    for word in wordlist:
        for ext in default_extensions:
            url = f'{target_url}/{word.strip()}{ext}'
            resp = attemptUrl(url)

            if resp in [200, 301, 302, 307, 308, 401, 403]:
                print('/' + word.strip() + f' ({str(resp)})')


def attemptUrl(target_url:  str):
    response = requests.head(target_url.strip(), allow_redirects=True)
    return response.status_code

if __name__ == "__main__":
    app()