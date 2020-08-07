import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton

class Main(QWidget):
    def __init__(self):
        super().__init__(None)

        self.setupUi()
        self.show()


    def setupUi(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("제목")
        self.record_button = QPushButton('button')
        layout = QVBoxLayout()
        self.record_button.clicked.connect(self.record_buttonClicked)
        layout.addWidget(self.record_button)
        self.setLayout(layout)

    def record_buttonClicked(self):
        print('buttonClicked')



app = QApplication(sys.argv)
mywindow = Main()
app.exec_()

