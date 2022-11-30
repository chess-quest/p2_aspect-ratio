from PyQt5.QtWidgets import *
from functions import *
from gui import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_go.clicked.connect(lambda: self.calculate())

    def calculate(self):
        try:
            ratio_width = int(self.aspect_width.text())
            ratio_height = int(self.aspect_height.text())
            value_width = float(self.input_width.text())
            value_height = float(self.input_height.text())
        except ValueError:
            self.label_output.setText(
                'broken')
        except:
            self.label_output.setText('error')
        else:
            self.label_output.setText('result')