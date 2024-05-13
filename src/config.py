from enum import Enum


class Config(Enum):
    CATEGORIES: tuple = ("food", "entertainment", "transport", "education")
    DATABASE_PATH: str = "./product_database.json"
    CLEARED_STRING: str = ""
    DEFAULT_WINDOW_POSITION_X: int = 100
    DEFAULT_WINDOW_POSITION_Y: int = 100
    DEFAULT_WINDOW_WIDTH: int = 1000
    DEFAULT_WINDOW_HEIGHT: int = 800
    MAX_WINDOW_WIDTH: int = 700
    MIN_WINDOW_HEIGHT: int = 500
    NUMBER_OF_PRODUCT_PROPERTIES: int = 3
    CANVAS_WIDTH: int = 5
    CANVAS_HEIGHT: int = 4
    CANVAS_DPI: int = 100
