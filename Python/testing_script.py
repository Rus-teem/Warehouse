"""Создаёт директорию для результатов парсинга."""

from pathlib import Path

path = Path("Parsing_results")
path.mkdir(parents=True, exist_ok=True)
print(f"Папка создана по пути: {path}")
