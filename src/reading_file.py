import csv
import logging
from pathlib import Path
from typing import Any, Hashable, Union

import pandas as pd

PATH_TO_ROOT = Path(__file__).parent.parent
PATH_TO_FILE = Path(PATH_TO_ROOT, "logs", "reading_files.log")


logger = logging.getLogger("reading_files")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH_TO_FILE, "w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_reading_csv(path_to_csv: Union[str, Path]) -> list[dict[str, Any]]:
    """Функция читает csv-файл и возвращает список словарей транзакций"""
    try:
        logger.info(f"Читаем файл: {path_to_csv}")
        with open(path_to_csv, encoding="UTF-8") as csv_file:
            reader_csv = csv.DictReader(csv_file, delimiter=";")
            data = [row for row in reader_csv]
            if not data:
                print("Файл пуст или содержит не корректные данные")
                logger.info("Файл пустой или не верные данные")
            logger.info(f"Функция {get_reading_csv.__name__} отработала корректно.")
            return data
    except FileNotFoundError as e:
        logger.info(f"Файл не найден с ошибкой {e}")
        return []


def get_reading_exel(path_to_exel: Union[str, Path]) -> list[dict[Hashable, Any]] | list[Any]:
    """Функция читает excel-файл и возвращает список словарей транзакций"""
    try:
        df = pd.read_excel(path_to_exel)
        dict_list = df.to_dict(orient="records")
        return dict_list
    except FileNotFoundError as e:
        logger.info(f"Файл не найден с ошибкой {e}")
        return []
