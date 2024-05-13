import src.model as model
import src.view as view


class Presenter:
    def __init__(self, model_object: model.Model, view_object: view.View) -> None:
        self.model = model_object
        self.view = view_object
        self.view.init_layout(self.model.database.all())

        self.view.try_add_product.connect(self.handle_input_data)
        self.view.try_clear_products.connect(self.handle_clear_data)

        self.model.invalid_product_data.connect(self.handle_invalid_product_data)
        self.model.products_updated.connect(self.handle_products_update)

    def handle_input_data(self, product: dict) -> None:
        self.model.add_product_to_database(product)

    def handle_clear_data(self) -> None:
        self.model.clear_database()

    def handle_invalid_product_data(self) -> None:
        self.view.display_error()

    def handle_products_update(self, products: list) -> None:
        self.view.update_layout(products)
        self.view.clear_inputs()
