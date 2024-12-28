import json
import os

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path_1)


# noinspection PyBroadException
def load_transactions(file_path: str) -> list[dict]:
    """Функция принимает json возвращает list или dict"""
    try:
        logger.debug(f"Открытие json файла {file_path}")
        with open(file_path, "r", encoding="Windows-1251") as file:
            repos = json.load(file)
            logger.debug(f"Проверяем, что файл {file_path} не пустой")
        if isinstance(repos, list):
            return repos
        else:
            return []
    except Exception:
        logger.error("Ошибка")
        return []
