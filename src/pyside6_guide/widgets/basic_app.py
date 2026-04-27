"""
basic_app.py
by Akhila Chitluri 
A simple calculator GUI app using PySide6 that takes two numeric inputs,
performs a selected operation, and displays the result with input validation.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QDoubleSpinBox,
    QComboBox,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator App")
        self.resize(350, 250)

        layout = QVBoxLayout()

        # Title
        title = QLabel("Simple Calculator")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        # Inputs (side by side)
        input_layout = QHBoxLayout()

        self.num1 = QDoubleSpinBox()
        self.num1.setRange(-100000, 100000)

        self.num2 = QDoubleSpinBox()
        self.num2.setRange(-100000, 100000)

        # Operation Dropdown
        self.operation = QComboBox()
        self.operation.addItems(["+", "-", "*", "/"])

        input_layout.addWidget(self.num1)
        input_layout.addWidget(self.operation)
        input_layout.addWidget(self.num2)

        # Buttons
        calc_button = QPushButton("Calculate")
        calc_button.clicked.connect(self.calculate)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_all)

        # Output
        self.output_label = QLabel("Enter numbers and choose an operation.")

        # Add widgets & layouts to main layout
        layout.addWidget(title)
        layout.addLayout(input_layout)
        layout.addWidget(calc_button)
        layout.addWidget(clear_button)
        layout.addWidget(self.output_label)

        layout.addStretch()

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calculate(self):
        num1 = self.num1.value()
        num2 = self.num2.value()
        op = self.operation.currentText()

        try:
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    self.output_label.setStyleSheet("color: red;")
                    self.output_label.setText("Error: Cannot divide by zero")
                    return
                result = num1 / num2

            result = round(result, 2)
            self.output_label.setStyleSheet("color: black;")
            self.output_label.setText(f"Result: {result}")

        except Exception:
            self.output_label.setStyleSheet("color: red;")
            self.output_label.setText("Error: Invalid input")

    def clear_all(self):
        self.num1.setValue(0)
        self.num2.setValue(0)
        self.output_label.setStyleSheet("color: black;")
        self.output_label.setText("Enter numbers and choose an operation.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()