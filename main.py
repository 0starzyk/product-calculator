import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from view import View
from model import Model
from presenter import Presenter
from tinydb import TinyDB, Query
from config import Config


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
