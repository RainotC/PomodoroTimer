import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QGridLayout, QWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer, QDateTime

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(300, 300, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowIcon(QIcon("clock.png"))
        self.setStyleSheet("background-color: #fae8e0;")
        self.initUI()

    def initUI(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        self.label = QLabel("Pomodoro timer", self)
        self.label.setFont(QFont("Arial", 20))
        self.label.setStyleSheet("color: #ef7c8e;"
                                 "font-weight: bold;")
        self.time_label = QLabel("", self)
        self.time_label.setFont(QFont("Arial", 20))
        self.time_label.setStyleSheet("color: #ef7c8e;"
                                 "font-weight: bold;")

        self.time_input_min = QLineEdit(self)
        self.time_input_min.setStyleSheet("font-size: 30px;")
        self.time_input_min.setPlaceholderText("Minutes")
        self.time_input_sec = QLineEdit(self)
        self.time_input_sec.setStyleSheet("font-size: 30px;")
        self.time_input_sec.setPlaceholderText("Seconds")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)

        self.startButton = QPushButton("Start", self)
        self.startButton.setStyleSheet("font-size: 30px;")
        self.startButton.clicked.connect(self.startTimer)

        self.stopButton = QPushButton("Stop", self)
        self.stopButton.setStyleSheet("font-size: 30px;")
        self.stopButton.clicked.connect(self.stopTimer)

        grid = QGridLayout()
        grid.addWidget(self.label, 0, 2, 1, 2, Qt.AlignCenter)
        grid.addWidget(self.time_input_min, 1, 2, 1, 1, Qt.AlignCenter)
        grid.addWidget(self.time_input_sec, 1, 3, 1, 1, Qt.AlignCenter)
        grid.addWidget(self.time_label, 2, 2, 1, 2, Qt.AlignCenter)
        grid.addWidget(self.startButton, 3, 0, 1, 1, Qt.AlignCenter)
        grid.addWidget(self.stopButton, 3, 4, 1, 1, Qt.AlignCenter)
        central_widget.setLayout(grid)

        self.countdown_time = None

    def showTime(self):
        if self.countdown_time > 0:
            self.countdown_time -= 1
            self.time_label.setText(self.format_time(self.countdown_time))
        else:
            self.timer.stop()
            self.time_label.setText("Time's up!")
            self.startButton.setEnabled(True)
            self.stopButton.setEnabled(False)

    def startTimer(self):
        minutes = self.time_input_min.text()
        seconds = self.time_input_sec.text()
        minutes_valid = minutes.isdigit() or minutes==''
        seconds_valid = seconds.isdigit() or seconds==''
        if (minutes_valid or seconds_valid) and (minutes!='' or seconds!=''):
            if minutes == '':
                minutes = 0
            if seconds == '':
                seconds = 0
            self.countdown_time = self.count_seconds(int(minutes), int(seconds))
            self.timer.start(1000)
            self.startButton.setEnabled(False)
            self.stopButton.setEnabled(True)
        else:
            self.time_label.setText("Please enter a valid number")


    def stopTimer(self):
        self.timer.stop()
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def count_seconds(self, minutes, seconds):
        return minutes*60 + seconds

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()