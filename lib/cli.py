import typer 
from lib.helpers import print_divider
from lib.database import Session
from lib.models import Flower
from lib.database import Sessions

app = typer.Typer()

@app.command()
def welcome():
    """Reet the user with a welcome message."""
    print_divider()
    typer.echo("Welcome to lush & bloom")
    typer.echo("Elegant Blooms, Everyday Joy.")
    print_divider()

    @app.command()
    def list_flowers():
        """List all flowers currently in the shop."""
        sessions = Sessions()
        flowers = sessions.query(Flower).all()

        if not flowers:
         typer.echo("No flowers found. Please seed the database.")
           

         for flower in flowers:   
           typer.echo(f"{flower.id}. {flower.name} ({flower.color}) -ksh {flower.price:.2f}") 

    if __name__ == "__main__":
        app()
