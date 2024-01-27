import typer
from utils import validateURL
from rich import print
import requests
from requests.exceptions import HTTPError

app = typer.Typer()

@app.command()
def main(target_url: str):
    print("Welcome to peek v0.1")

    # Checking if target url is a valid url
    if validateURL(target_url):
        try:
            response = requests.get(target_url, timeout=1)

        except HTTPError as http_err:
            print('Target does not appear to be up.')
        except Exception as err:
            print('Target does not appear to be up.')
        else:
            if response.status_code == 200:
                print('Target website up!')
    else:
        print('URL seems to be badly formed!')


if __name__ == "__main__":
    app()