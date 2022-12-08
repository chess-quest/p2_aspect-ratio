import PIL
from PyQt5.QtWidgets import *
from functions import *
from view import *
from PIL import Image


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
        self.pushButton_preview.clicked.connect(lambda: self.image_manip(0))
        self.pushButton_save.clicked.connect(lambda: self.image_manip(1))

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
        val_multiplier = clean_input(self.lineEdit_Multiplyer.text())
        val_height = clean_input(self.lineEdit_height.text())
        val_width = clean_input(self.lineEdit_width.text())
        if val_width == 0 or val_height == 0 or val_multiplier == 0:
            self.label_output.setText("Please enter non-zero values")
            return
        else:
            self.lineEdit_height.setText(f'{val_multiplier * val_height}')
            self.lineEdit_width.setText(f'{val_multiplier * val_width}')

    def check_empty_values(self):
        val_width = clean_input(self.lineEdit_width.text())
        val_height = clean_input(self.lineEdit_height.text())
        if val_width == 0 or\
                val_height == 0:
            raise ValueError
        else:
            return round(val_width), round(val_height)

    def image_manip(self, mode_value):
        filename = self.lineEdit_filename.text()
        try:
            size = self.check_empty_values()
            with Image.open(filename) as img:
                img.load()
                filter_num = self.get_radio_button()
                img_changed = img.resize(size, resample=filter_num)
                if mode_value == 0:
                    img_changed.show()
                else:
                    img_changed.save(f'{filename[:-4]}_{size}.png')
        except FileNotFoundError:
            self.label_output.setText('Given file does not exist\nin this directory')
        except AttributeError:
            self.label_output.setText('Please enter a file name')
        except PIL.UnidentifiedImageError:
            self.label_output.setText('Given file is not a readable\nimage format')
        except ValueError:
            self.label_output.setText("Please enter non-zero values")

    def get_radio_button(self):
        if self.radioButton_nearest.isChecked():
            return 0
        elif self.radioButton_lanczos.isChecked():
            return 1
        elif self.radioButton_bilinear.isChecked():
            return 2
        elif self.radioButton_Bicubic.isChecked():
            return 3
        elif self.radioButton_box.isChecked():
            return 4
        else:
            return 5
