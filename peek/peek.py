import typer
from rich import print
import requests

app = typer.Typer()

@app.command()
def main(target_utl: str):
    print("Welcome to peek v0.1")

    response = requests.get(target_utl)
    if response.status_code == 200:
        print('Target website up!')
    else:
        print('Target does not appear to be up')


if __name__ == "__main__":
    app()