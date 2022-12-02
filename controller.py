from PyQt5.QtWidgets import *
from functions import *
from view import *


def clean_input(value):
    try:
        value = float(value)
    except ValueError:
        return 0
    else:
        return value


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.lineEdit_width.textEdited.connect(lambda: self.calc_from_width())
        self.lineEdit_height.textEdited.connect(lambda: self.calc_from_height())
        self.lineEdit_aspect_width.textEdited.connect(lambda: self.calc_from_height())
        self.lineEdit_aspect_height.textEdited.connect(lambda: self.calc_from_width())
        self.pushButton_multiplier.clicked.connect(lambda: self.multiply())

    def calc_from_width(self):
        self.label_output.setText("")
        val_width = clean_input(self.lineEdit_width.text())
        val_aspect_width = clean_input(self.lineEdit_aspect_width.text())
        val_aspect_height = clean_input(self.lineEdit_aspect_height.text())
        if val_width == 0 or val_aspect_width == 0 or val_aspect_height == 0:
            self.label_output.setText("Please enter non-zero values")
            return
        else:
            val_height = height_from_width(
                val_width, val_aspect_width, val_aspect_height
            )
            self.lineEdit_height.setText(f'{val_height}')

    def calc_from_height(self):
        self.label_output.setText("")
        val_height = clean_input(self.lineEdit_height.text())
        val_aspect_width = clean_input(self.lineEdit_aspect_width.text())
        val_aspect_height = clean_input(self.lineEdit_aspect_height.text())
        if val_height == 0 or val_aspect_width == 0 or val_aspect_height == 0:
            self.label_output.setText("Please enter non-zero values")
            return
        else:
            val_width = width_from_height(
                val_height, val_aspect_width, val_aspect_height
            )
            self.lineEdit_width.setText(f'{val_width}')

    def multiply(self):
        val_multiplier = clean_input(self.lineEdit_multiplier.text())
        val_height = clean_input(self.lineEdit_height.text())
        val_width = clean_input(self.lineEdit_width.text())
        if val_width == 0 or val_height == 0 or val_multiplier == 0:
            self.label_output.setText("Please enter non-zero values")
            return
        else:
            self.lineEdit_height.setText(f'{val_multiplier * val_height}')
            self.lineEdit_width.setText(f'{val_multiplier * val_width}')
