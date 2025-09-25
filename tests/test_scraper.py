from pathlib import Path
import os
import pytest

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


def test_scraper_wikipedia_nonexistent(tmp_path: Path):
    out_file = tmp_path / "nonexistent.txt"
    title = run("asdkjhasdkjhaskjdh", str(out_file))
    assert "Wikipedia" in title or "not found" in title.lower()
    assert out_file.exists(), "O arquivo de saída não foi criado"


def test_scraper_output_content(tmp_path: Path):
    out_file = tmp_path / "aristotle.txt"
    run("Aristotle", str(out_file))
    content = out_file.read_text()
    assert "Aristotle" in content or len(content) > 50


def test_scraper_overwrite_file(tmp_path: Path):
    out_file = tmp_path / "plato.txt"
    out_file.write_text("old content")
    run("Plato", str(out_file))
    content = out_file.read_text()
    assert "old content" not in content


def test_scraper_invalid_path():
    with pytest.raises(Exception):
        run("Socrates", "/invalid/path/socrates.txt")
