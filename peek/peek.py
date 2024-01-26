import typer
from rich import print
import requests
from requests.exceptions import HTTPError

app = typer.Typer()

@app.command()
def main(target_utl: str):
    print("Welcome to peek v0.1")

    try:
        response = requests.get(target_utl, timeout=1)

    except HTTPError as http_err:
        print('Target does not appear to be up.')
    except Exception as err:
        print('Target does not appear to be up.')
    else:
        if response.status_code == 200:
            print('Target website up!')


if __name__ == "__main__":
    app()