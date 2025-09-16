from pathlib import Path
import os

# importa a função principal do teu scraper
from src.bot import run


def test_scraper_wikipedia_kant(tmp_path: Path):
    # saída temporária na pasta de teste
    out_file = tmp_path / "kant.txt"

    # executa o fluxo real do scraper (headless)
    title = run("Immanuel Kant", str(out_file))

    # asserções simples e resilientes
    assert "Kant" in title or "Wikipedia" in title
    assert out_file.exists(), "O arquivo de saída não foi criado"
