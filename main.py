import sys
from PyQt5 import QtWidgets
from tinydb import TinyDB
from src.view import View
from src.model import Model
from src.presenter import Presenter
from src.config import Config


def main():
    app = QtWidgets.QApplication(sys.argv)
    database = TinyDB(Config.DATABASE_PATH.value)
    model = Model(database)
    view = View()
    presenter = Presenter(model, view)
    view.show()
    app.exec()
    database.close()
    sys.exit()


if __name__ == "__main__":
    main()
