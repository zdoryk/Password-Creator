from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Custom fonts
text_font = QFont()
text_font.setFamily(u"Futura Hv BT")
text_font.setPointSize(16)

check_font = QFont()
check_font.setFamily(u"Futura Hv BT")
check_font.setPointSize(14)

# Custom styleSheet for different statuses of our checkbox

UNCHECKED = u"border-color: #B9B1D9;\n" \
            "border-width: 2px;\n" \
            "border-style: solid;\n" \
            "border-radius: 10px;"

CHECKED = u"background-color: #5834EA;\n" \
          "border-radius: 10px;" \
          "text-align: center;"


# My representation of QCheckBox
class MyCheckbox(QWidget):
    def __init__(self, parent, text: str, checked: bool = True):
        super().__init__(parent=parent)
        # Represents checkbox status
        self.checked = checked
        # Draw my checkbox
        self.square = QLabel(self)
        self.square.setGeometry(QRect(0, 0, 35, 35))
        self.square.setFont(check_font)
        self.square.setAlignment(Qt.AlignCenter)
        self.set_state()

        # Text near rectangle
        self.text = QLabel(text, self)
        self.text.setGeometry(QRect(60, 0, 230, 35))
        self.text.setFont(text_font)
        # Changes status of checkbox when user clicked on it
        self.mouseReleaseEvent = self.change_state

    # Change how the rectangle looks
    def set_state(self):
        if self.checked:
            self.square.setStyleSheet(CHECKED)
            self.square.setText(u"\u2716")
        else:
            self.square.setStyleSheet(UNCHECKED)
            self.square.setText("")

    # Switch status of checkbox from True to False or on the contrary
    def change_state(self, event: QMouseEvent):
        self.checked = not self.checked
        self.set_state()
