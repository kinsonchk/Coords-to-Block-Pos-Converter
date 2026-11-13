import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *

#import converter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # App window setup
        self.setWindowTitle("Coords to Block Position Converter")
        #self.setFixedSize(QSize(400, 400))

        # Setup GUI
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # GUI Components
        layout.addWidget(QLabel("Step 1: Coords (in real life) boundary info"))

        layout.addWidget(QLabel("Westernmost coord (LONG)"))
        self.min_x_str = QLineEdit()
        self.min_x_str.setPlaceholderText("-74.0")
        layout.addWidget(self.min_x_str)

        layout.addWidget(QLabel("Southernmost coord (LAT)"))
        self.min_y_str = QLineEdit()
        self.min_y_str.setPlaceholderText("45.4")
        layout.addWidget(self.min_y_str)

        layout.addWidget(QLabel("Easternmost coord (LONG)"))
        self.max_x_str = QLineEdit()
        self.max_x_str.setPlaceholderText("-73.4")
        layout.addWidget(self.max_x_str)

        layout.addWidget(QLabel("Northernmost coord (LAT)"))
        self.max_y_str = QLineEdit()
        self.max_y_str.setPlaceholderText("45.7")
        layout.addWidget(self.max_y_str)


        layout.addWidget(QLabel("Step 2: Block (in Minecraft map) boundary info"))

        layout.addWidget(QLabel("Left block of the map boundary (X)"))
        self.left_str = QLineEdit()
        self.left_str.setPlaceholderText("0")
        layout.addWidget(self.left_str)

        layout.addWidget(QLabel("Top block of the map boundary (Z)"))
        self.top_str = QLineEdit()
        self.top_str.setPlaceholderText("0")
        layout.addWidget(self.top_str)

        layout.addWidget(QLabel("Right block of the map boundary (X)"))
        self.right_str = QLineEdit()
        self.right_str.setPlaceholderText("8900")
        layout.addWidget(self.right_str)

        layout.addWidget(QLabel("Bottom block of the map boundary (Z)"))
        self.bottom_str = QLineEdit()
        self.bottom_str.setPlaceholderText("5400")
        layout.addWidget(self.bottom_str)


        layout.addWidget(QLabel("Step 3: Target Minecraft block position in real-life coords"))

        layout.addWidget(QLabel("Target coord (LAT)"))
        self.pos_y_str = QLineEdit()
        self.pos_y_str.setPlaceholderText("45.470358")
        layout.addWidget(self.pos_y_str)

        layout.addWidget(QLabel("Target coord (LONG)"))
        self.pos_x_str = QLineEdit()
        self.pos_x_str.setPlaceholderText("-73.538817")
        layout.addWidget(self.pos_x_str)


        convert_button = QPushButton("Convert Coords")
        convert_button.clicked.connect(self.convert_coords)
        layout.addWidget(convert_button)

        reset_button = QPushButton("Clear Fields")
        reset_button.clicked.connect(self.clear_fields)
        layout.addWidget(reset_button)

        layout.addWidget(QLabel("Result"))

    def convert_coords(self):
        user_input = self.pos_x_str.text()
        print(f"Convert coords button clicked with input: {user_input}")

    def clear_fields(self):
        self.min_x_str.clear()
        self.min_y_str.clear()
        self.max_x_str.clear()
        self.max_y_str.clear()
        self.left_str.clear()
        self.top_str.clear()
        self.right_str.clear()
        self.bottom_str.clear()
        self.pos_y_str.clear()
        self.pos_x_str.clear()
        print("Clear fields button clicked")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

if __name__ == "__main__":
    app.exec()