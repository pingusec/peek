import typer
from rich import print

app = typer.Typer()

@app.command()
def main():
    print("Welcome to peek v0.1")

if __name__ == "__main__":
    app()