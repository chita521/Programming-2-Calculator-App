"""
basic_app.py
by Akhila Chitluri 
A simple calculator GUI app using PySide6 that takes two numeric inputs,
performs a selected operation, and displays the result with input validation.
"""

import sys
from PySide6.QtCore import Qt
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

        # Title label 
        title = QLabel("Simple Calculator")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        # Input section
        input_layout = QHBoxLayout()
        input_layout.setAlignment(Qt.AlignTop)

        # First number input
        self.num1 = QDoubleSpinBox()
        self.num1.setRange(-100000, 100000)

        # Operation Dropdown
        self.operation = QComboBox()
        self.operation.addItems(["+", "-", "*", "/"])
        
        # Second number input
        self.num2 = QDoubleSpinBox()
        self.num2.setRange(-100000, 100000)

        # Labels for inputs 
        label1 = QLabel("Number 1:")
        label2 = QLabel("Number 2:")

        # Group first input
        left_layout = QVBoxLayout()
        left_layout.addWidget(label1)
        left_layout.addWidget(self.num1)
        left_layout.setAlignment(Qt.AlignTop)

        # Group second input 
        right_layout = QVBoxLayout()
        right_layout.addWidget(label2)
        right_layout.addWidget(self.num2)
        right_layout.setAlignment(Qt.AlignTop)

        # Operation label & layout
        op_label = QLabel("Operation")

        op_layout = QVBoxLayout()
        op_layout.addWidget(op_label)
        op_layout.addWidget(self.operation)
        op_layout.setAlignment(Qt.AlignTop)

        # Add everything aligned
        input_layout.addLayout(left_layout)
        input_layout.addLayout(op_layout)
        input_layout.addLayout(right_layout)

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
        """Handles calculation and updates output label"""
        num1 = self.num1.value()
        num2 = self.num2.value()
        op = self.operation.currentText()

        try:
            # Perform selected operation
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

            # Round result for cleaner output 
            result = round(result, 2)

            # Display result 
            self.output_label.setStyleSheet("color: black;")
            self.output_label.setText(f"Result: {result}")

        except Exception:
            self.output_label.setStyleSheet("color: red;")
            self.output_label.setText("Error: Invalid input")

    def clear_all(self):
        """Resets inputs and output label"""

        self.num1.setValue(0)
        self.num2.setValue(0)
        self.output_label.setStyleSheet("color: black;")
        self.output_label.setText("Enter numbers and choose an operation.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()