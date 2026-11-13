import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *

import converter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # App window setup
        self.setWindowTitle("Coords to Block Position Converter")

        # Setup GUI
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)


        # GUI Components
        main_layout.addSpacing(10)
        group_box_1 = QGroupBox("Step 1: Coords (in real life) boundary info")
        form_layout_1 = QFormLayout()

        group_box_1.setLayout(form_layout_1)
        main_layout.addWidget(group_box_1)

        form_layout_1.addRow(QLabel("Westernmost coord (LONG)"))
        self.min_x_str = QLineEdit()
        self.min_x_str.setPlaceholderText("-74.0")
        form_layout_1.addWidget(self.min_x_str)

        form_layout_1.addRow(QLabel("Southernmost coord (LAT)"))
        self.min_y_str = QLineEdit()
        self.min_y_str.setPlaceholderText("45.4")
        form_layout_1.addWidget(self.min_y_str)

        form_layout_1.addRow(QLabel("Easternmost coord (LONG)"))
        self.max_x_str = QLineEdit()
        self.max_x_str.setPlaceholderText("-73.4")
        form_layout_1.addWidget(self.max_x_str)

        form_layout_1.addRow(QLabel("Northernmost coord (LAT)"))
        self.max_y_str = QLineEdit()
        self.max_y_str.setPlaceholderText("45.7")
        form_layout_1.addWidget(self.max_y_str)


        main_layout.addSpacing(10)
        group_box_2 = QGroupBox("Step 2: Block (in Minecraft map) boundary info")
        form_layout_2 = QFormLayout()

        group_box_2.setLayout(form_layout_2)
        main_layout.addWidget(group_box_2)
    
        form_layout_2.addRow(QLabel("Left block of the map boundary (X)"))
        self.left_str = QLineEdit()
        self.left_str.setPlaceholderText("0")
        form_layout_2.addWidget(self.left_str)

        form_layout_2.addRow(QLabel("Top block of the map boundary (Z)"))
        self.top_str = QLineEdit()
        self.top_str.setPlaceholderText("0")
        form_layout_2.addWidget(self.top_str)

        form_layout_2.addRow(QLabel("Right block of the map boundary (X)"))
        self.right_str = QLineEdit()
        self.right_str.setPlaceholderText("8900")
        form_layout_2.addWidget(self.right_str)

        form_layout_2.addRow(QLabel("Bottom block of the map boundary (Z)"))
        self.bottom_str = QLineEdit()
        self.bottom_str.setPlaceholderText("5400")
        form_layout_2.addWidget(self.bottom_str)


        main_layout.addSpacing(10)
        group_box_3 = QGroupBox("Step 3: Target Minecraft block position in real-life coords")
        form_layout_3 = QFormLayout()

        group_box_3.setLayout(form_layout_3)
        main_layout.addWidget(group_box_3)

        form_layout_3.addRow(QLabel("Target coord (LAT)"))
        self.pos_y_str = QLineEdit()
        self.pos_y_str.setPlaceholderText("45.470358")
        form_layout_3.addWidget(self.pos_y_str)

        form_layout_3.addRow(QLabel("Target coord (LONG)"))
        self.pos_x_str = QLineEdit()
        self.pos_x_str.setPlaceholderText("-73.538817")
        form_layout_3.addWidget(self.pos_x_str)


        convert_button = QPushButton("Convert Coords")
        convert_button.clicked.connect(self.convert_coords)
        main_layout.addWidget(convert_button)

        reset_button = QPushButton("Reset Fields")
        reset_button.clicked.connect(self.clear_fields)
        main_layout.addWidget(reset_button)


        main_layout.addSpacing(10)
        group_box_4 = QGroupBox("RESULT")
        form_layout_4 = QFormLayout()

        group_box_4.setLayout(form_layout_4)
        main_layout.addWidget(group_box_4)

        self.result_label = QLabel("Awaiting conversion...\n")
        form_layout_4.addRow(self.result_label)

    def convert_coords(self):
        print("Convert coords button clicked")

        result_str = converter.convert(
            self.min_x_str.text(),
            self.min_y_str.text(),
            self.max_x_str.text(),
            self.max_y_str.text(),
            self.left_str.text(),
            self.top_str.text(),
            self.right_str.text(),
            self.bottom_str.text(),
            self.pos_y_str.text(),
            self.pos_x_str.text()
        )
        self.result_label.setText(result_str)

    def clear_fields(self):
        print("Reset fields button clicked")

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
        self.result_label.setText("Awaiting conversion...")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

if __name__ == "__main__":
    app.exec()