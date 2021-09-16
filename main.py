from PySide2 import QtWidgets, QtGui
import sys
import main_window
from random import sample, randrange

# Main window creation
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
QtGui.QFontDatabase.addApplicationFont('Futura Heavy BT.ttf')
ui = main_window.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


# Password generation function
def password_generation():
    # I created a list with all 4 checkboxes.
    # This list contains 4 lists in which:
    #   [0] Checkbox status ( True/False )
    #   [1] Reference to function ( I wrote 4 different functions for every checkbox )

    checkbox_list = [[ui.number_checkbox.checked, number_func],
                     [ui.lwr_str_checkbox.checked, lower_string_func],
                     [ui.uppr_str_checkbox.checked, upper_string_func],
                     [ui.spec_symb_checkbox.checked, special_symbols_func]]

    # Clean our list from all lists with [0] == False
    checkbox_list = list(filter(lambda x: x[0] is True, checkbox_list))

    if len(checkbox_list) == 0:
        ui.password_text_edit.setText('Please choose at least 1 option')
    else:
        # Get length of our future password
        char_amount = int(ui.char_amount_label.text())

        generated_password = ''

        # Wrote a length distribution with randrange because I want to randomize it more
        for i in range(len(checkbox_list) - 1):
            generated_password += checkbox_list[i][1](randrange(1, int((char_amount - len(generated_password)) / 2)))

        # Last string from checkbox_list[1] must contains remaining number of chars
        generated_password += checkbox_list[-1][1](char_amount - len(generated_password))
        # Shuffle to randomize it even more!
        generated_password = "".join(sample(generated_password, len(generated_password)))

        print(f"{generated_password=} | length: {len(generated_password)}")
        # Show to user generated password
        ui.password_text_edit.setText(generated_password)


# Wrote this 4 functions in same way
# Use Ascii table to take required range of int's and then put them to chr()
def number_func(char_amount: int) -> str:
    result = ''
    for i in range(char_amount):
        result += chr(randrange(48, 57))
    return result


def lower_string_func(char_amount: int) -> str:
    result = ''
    for i in range(char_amount):
        result += chr(randrange(97, 122))
    return result


def upper_string_func(char_amount: int) -> str:
    result = ''
    for i in range(char_amount):
        result += chr(randrange(65, 90))
    return result


def special_symbols_func(char_amount: int) -> str:
    result = ''
    for i in range(char_amount):
        result += chr(randrange(33, 47))
    return result


# Button connection

ui.generate_btn.clicked.connect(password_generation)

sys.exit(app.exec_())
