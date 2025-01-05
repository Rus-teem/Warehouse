
from pathlib import Path


# Указываем путь для создания папки
path = Path("C:/Projects/Warehouse/Parsing_results")

# Создаем папку
path.mkdir(parents=True, exist_ok=True)

print(f"Папка создана по пути: {path}")


