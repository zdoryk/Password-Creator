from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Style for slider wrote on QSS
style = """
    QSlider::groove:horizontal {{
        border-radius: 5px;
        height: 15px;
        margin: 0px;
        background-color: rgb(52, 59, 72);
    }}
    QSlider::groove:horizontal:hover {{
        background-color: rgb(55, 62, 76);
    }}
    QSlider::handle:horizontal {{
        background-color: #8b74e3;
        border: none;
        height: 15px;
        width: 15px;
        margin: 0px;
        border-radius: 7px;
    }}
    QSlider::handle:horizontal:hover {{
        background-color: #5834EA;
    }}
    QSlider::handle:horizontal:pressed {{
        background-color: #5834EA;
    }}
"""


# My representation of QSlider
class PySlider(QSlider):
    def __init__(
            self, orientation, parent
    ):
        super().__init__(orientation=orientation, parent=parent)

        # Set my style
        self.setStyleSheet(style.format())