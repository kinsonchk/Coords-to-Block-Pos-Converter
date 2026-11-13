import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *

#import converter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # App window setup
        self.setWindowTitle("Coords to Block Position Converter")
        self.setFixedSize(QSize(400, 400))

        # Setup GUI
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # GUI Components
        label = QLabel("Welcome!")
        layout.addWidget(label)
        
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Type here...")
        layout.addWidget(self.line_edit)

        convert_button = QPushButton("Convert Coords")
        convert_button.clicked.connect(self.convert_coords)
        layout.addWidget(convert_button)

        reset_button = QPushButton("Clear Fields")
        reset_button.clicked.connect(self.reset_fields)
        layout.addWidget(reset_button)

    def convert_coords(self):
        user_input = self.line_edit.text()
        print(f"Convert coords button clicked with input: {user_input}")

    def reset_fields(self):
        self.line_edit.clear()
        print("Clear fields button clicked")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

if __name__ == "__main__":
    app.exec()