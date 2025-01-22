import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from modules.main_window import Ui_MainWindow
from modules.store_module import add_product

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_store_tab()

    def setup_store_tab(self):
        self.ui.add_product_button.clicked.connect(self.add_product)

    def add_product(self):
        product_name = self.ui.product_name_input.text()
        vendor_id = int(self.ui.vendor_id_input.text())
        quantity = int(self.ui.quantity_input.text())
        price_per_unit = float(self.ui.price_input.text())
        result = add_product(product_name, vendor_id, quantity, price_per_unit)
        self.ui.statusBar.showMessage(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())