from PyQt6.QtWidgets import QApplication, QWidget,\
    QLineEdit,QSpinBox, QHBoxLayout, QLabel
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 SpinBox")
        self.setGeometry(500,200, 500,400)

        self.create_spinbox()

    def create_spinbox(self):
        hbox = QHBoxLayout()

        label = QLabel("Car Price : ")

        self.lineEdit = QLineEdit()

        self.spinbox = QSpinBox()

        self.spinbox.valueChanged.connect(self.spin_selected)
        self.totalResult = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.totalResult)

        self.setLayout(hbox)

    def spin_selected(self):
        if self.lineEdit.text() != 0:
            price = int(self.lineEdit.text())
            totalPrice = self.spinbox.value() * price

            self.totalResult.setText(str(totalPrice))


        else:
            print("Wrong value")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())