#!/usr/bin/env python3
"""Script para descargar y guardar en JSON tablas de html"""

import typer
import pandas as pd

app = typer.Typer()

@app.command()
def scrap_table(url: str):
    data = pd.read_html(url)
    for idx, table in enumerate(data):
        table.to_csv(f'table{idx}.csv')

if __name__ == '__main__':
    app()