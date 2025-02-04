from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton


class statsWindow(QWidget):
    def __init__(self, stacked_widget):
        super(statsWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Store reference to QStackedWidget
        self.setWindowTitle("Statistics")
        self.setStyleSheet("background-color: #f0f0f0;")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Statistics Page", self)
        self.label.setStyleSheet("font-size: 20px; color: #333; font-weight: bold;")

        self.back_button = QPushButton("Back to Timer", self)
        self.back_button.setStyleSheet("font-size: 16px;")
        self.back_button.clicked.connect(self.goBack)

        layout.addWidget(self.label)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

    def goBack(self):
        self.stacked_widget.setCurrentIndex(0)