import os
import time
import typer
import requests
from rich import print
from rich.table import Table
from rich.console import Console
from typing_extensions import Annotated
from utils import validateURL, UrlStatus

version = '0.1'
app = typer.Typer()
console = Console()

@app.command()
def main(target_url: Annotated[str, typer.Argument()], wordlist_path: Annotated[str, typer.Argument()]):
    err = True
    prog_output  = Table(f'Welcome to peek v{version}')

    # Checking if target url is a valid url and is reachable and if the wordlist exists
    match validateURL(target_url):
        case UrlStatus.UNREACHABLE:
            prog_output.add_row(f'Target url ({target_url}) seems to be unreachable.')
        
        case UrlStatus.BADLY_FORMED:
            prog_output.add_row(f'The target {target_url} appears to be a badly formed URL.')
        
        case UrlStatus.UP:
            prog_output.add_row(f'Target url: {target_url} (seems to be up!)')
        
            if os.path.exists(wordlist_path):
                err = False
                console.print(prog_output)
                print('[red]> NOTE: These requests can be monitored by the web server. They are not invisible.')
                dirRecon(target_url, wordlist_path)
        
            else:
                prog_output.add_row('Wordlist file "%s" does not exist.', wordlist_path)
    if err: console.print(prog_output)

def dirRecon(target_url: str, wordlist_path: str):
    print('============================')
    print('[bold green][+][/bold green] Starting directory recon')
    print('============================')

    default_extensions = ['/', '.html', '.htm', '.php', '.js', '.jsx', '.pdf']

    wordlist = open(wordlist_path, 'r')

    start_time = time.time()

    for word in wordlist:
        for ext in default_extensions:
            url = f'{target_url}/{word.strip()}{ext}'
            resp = attemptUrl(url)

            if resp in [200, 301, 302, 307, 308, 401, 403]:
                print('> /' + word.strip() + f' ({str(resp)})')

    end_time = time.time()
    print('============================')
    print(f'[bold green][+][/bold green] Finished in {round(end_time - start_time, 2)}s')
    print('============================')

def attemptUrl(target_url:  str):
    response = requests.head(target_url.strip(), allow_redirects=True)
    return response.status_code

if __name__ == "__main__":
    app()