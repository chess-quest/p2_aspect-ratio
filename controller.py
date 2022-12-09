import PIL
from PyQt5.QtWidgets import *
from functions import *
from view import *
from PIL import Image

QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)


def clean_input(value: str) -> float:
    """
    Takes a given string and will return
    it as a float if it can, else it returns a
    zero
    :param value: the given string
    :return: a float from the string
    """
    try:
        value = float(value)
    except ValueError:
        return 0
    else:
        return value


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        """
        A class that controls the gui
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.lineEdit_width.textEdited.connect(lambda: self.calc_from_width())
        self.lineEdit_height.textEdited.connect(lambda: self.calc_from_height())
        self.lineEdit_aspect_width.textEdited.connect(lambda: self.calc_from_height())
        self.lineEdit_aspect_height.textEdited.connect(lambda: self.calc_from_width())
        self.pushButton_multiplier.clicked.connect(lambda: self.multiply())
        self.pushButton_preview.clicked.connect(lambda: self.image_manip(0))
        self.pushButton_save.clicked.connect(lambda: self.image_manip(1))

    def calc_from_width(self) -> None:
        """
        Function that calculates height when the width is updated
        :return: None
        """
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

    def calc_from_height(self) -> None:
        """
        Function that calculates width when the height is updated
        :return: None
        """
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

    def multiply(self) -> None:
        """
        Function that will update the height and width when given a multiplier
        :return: None
        """
        val_multiplier = clean_input(self.lineEdit_Multiplyer.text())
        val_height = clean_input(self.lineEdit_height.text())
        val_width = clean_input(self.lineEdit_width.text())
        if val_width == 0 or val_height == 0 or val_multiplier == 0:
            self.label_output.setText("Please enter non-zero values")
            return
        else:
            self.lineEdit_height.setText(f'{val_multiplier * val_height}')
            self.lineEdit_width.setText(f'{val_multiplier * val_width}')

    def check_empty_values(self) -> tuple[int, int]:
        """
        Function that will make sure the height and width aren't
        empty and return them afterwards or raise an error
        :return: two ints
        """
        val_width = clean_input(self.lineEdit_width.text())
        val_height = clean_input(self.lineEdit_height.text())
        if val_width == 0 or\
                val_height == 0:
            raise ValueError
        else:
            return round(val_width), round(val_height)

    def image_manip(self, mode_value: int) -> None:
        """
        Function that when will take an input file, and resize it to the given width and height using the selected
        resample filter
        :param mode_value: an int that determines whether the image is previewed (0), or saved (1)
        :return: None
        """
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
            self.label_output.setText("Please enter a greater than zero\npositive integer")

    def get_radio_button(self) -> int:
        """
        Function that will check the state of the radio buttons and return an int representative of that radio button
        :return: an int pertaining to a radio button
        """
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
