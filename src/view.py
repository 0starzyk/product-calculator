from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal
import src.utils as utils
import src.piecanvas as piecanvas
from src.config import Config


class View(QMainWindow):
    try_add_product = pyqtSignal(dict)
    try_clear_products = pyqtSignal()

    def __init__(self):
        super(View, self).__init__()
        self.categories = Config.CATEGORIES.value

        self.setWindowTitle("Product calculator")
        self.setGeometry(Config.DEFAULT_WINDOW_POSITION_X.value, Config.DEFAULT_WINDOW_POSITION_Y.value,
                         Config.DEFAULT_WINDOW_WIDTH.value, Config.DEFAULT_WINDOW_HEIGHT.value)
        self.setMinimumSize(Config.MAX_WINDOW_WIDTH.value, Config.MIN_WINDOW_HEIGHT.value)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)

        text_widget = QLabel("Product calculator")
        text_widget.setStyleSheet("font-weight: 300; font-size: 40px; font-weight: bold; text-transform: uppercase;")
        text_widget.setAlignment(Qt.AlignHCenter)
        main_layout.addWidget(text_widget)

        product_widget = QWidget()
        product_layout = QFormLayout(product_widget)
        self.name_input = QLineEdit()
        product_layout.addRow("Name", self.name_input)
        self.price_input = QDoubleSpinBox()
        self.price_input.setSuffix(" PLN")
        product_layout.addRow("Price", self.price_input)
        self.category_input = QComboBox()
        self.category_input.addItems(self.categories)
        product_layout.addRow("Category", self.category_input)
        product_widget.setLayout(product_layout)
        main_layout.addWidget(product_widget)

        add_button = QPushButton()
        add_button.setText("Add product")
        main_layout.addWidget(add_button)

        clear_button = QPushButton()
        clear_button.setText("Clear products")
        main_layout.addWidget(clear_button)

        self.error_widget = QLabel("Invalid input")
        self.error_widget.setStyleSheet("color: red")
        self.error_widget.hide()
        main_layout.addWidget(self.error_widget)

        self.product_list = QListWidget()
        main_layout.addWidget(self.product_list)

        self.circle_diagram = piecanvas.PieCanvas()
        main_layout.addWidget(self.circle_diagram)

        main_widget = QWidget()
        main_widget.setStyleSheet("font-family: Courier; font-size: 24px;")
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        add_button.clicked.connect(self.on_add_button_clicked)
        clear_button.clicked.connect(self.on_clear_button)

    def on_add_button_clicked(self):
        name = self.name_input.text()
        price = self.price_input.value()
        category = self.category_input.currentText()
        product = {"name": name, "price": price, "category": category}
        self.error_widget.hide()
        self.try_add_product.emit(product)

    def on_clear_button(self):
        self.try_clear_products.emit()

    def display_error(self):
        self.error_widget.show()

    def clear_inputs(self):
        self.name_input.setText(Config.CLEARED_STRING.value)
        self.price_input.setValue(0.0)
        self.error_widget.hide()

    def update_table(self, products: list):
        self.product_list.clear()
        if len(products) == 0:
            return
        for index, product in enumerate(products):
            list_item = QListWidgetItem(
                f"product: {product['name']}, price: {product['price']} PLN, category: {product['category']}")
            self.product_list.addItem(list_item)

    def update_plot(self, products: list):
        values, labels = utils.get_values_and_labels_from_products(products)
        self.circle_diagram.axes.cla()
        self.circle_diagram.axes.pie(values, labels=labels, autopct=utils.autopct_format(values))
        self.circle_diagram.draw()

    def update_layout(self, products: list):
        self.update_table(products)
        self.update_plot(products)

    def init_layout(self, products: list):
        self.update_layout(products)
