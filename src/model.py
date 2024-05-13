from PyQt5.QtCore import QObject, pyqtSignal
from tinydb import TinyDB
import utils


class Model(QObject):
    invalid_product_data = pyqtSignal()
    products_updated = pyqtSignal(list)

    def __init__(self, database: TinyDB):
        super(Model, self).__init__()
        self.database = database

    def add_product_to_database(self, product_data: dict) -> None:
        if utils.is_valid_product_data(product_data):
            self.database.insert(product_data)
            self.products_updated.emit(self.database.all())
        else:
            self.invalid_product_data.emit()

    def clear_database(self) -> None:
        self.database.truncate()
        self.products_updated.emit(self.database.all())
