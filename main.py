from datetime import datetime
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QVBoxLayout, QWidget)
from pytz import timezone


class WorldClockApp(QWidget):
    def __init__(self):
        super().__init__()

        # Mapping of timezone abbreviations to their respective timezone
        self.mapping = {
            "CST": "America/Chicago",
            "PST": "America/Los_Angeles",
            "EST": "America/New_York",
            "GMT": "Europe/London",
            "CET": "Europe/Berlin",
            "IST": "Asia/Kolkata",
            "JST": "Asia/Tokyo",
        }

        """
        Initializing the UI and starting the timer. This will create the main layout
        and add the CST clock at the top with 6 more clocks below it. The timer will
        update the time every second.
        """
        self.init_UI()
        self.start_timer()

    # Helper method used to get the current time in a specific timezone
    def get_time_by_zone(self, zone):
        tz = timezone(zone)
        return datetime.now(tz).strftime("%H:%M:%S")

    def init_UI(self):
        self.setWindowTitle("World Clock")
        self.setGeometry(100, 100, 400, 400)

        self.main_layout = QVBoxLayout()

        # Create the CST clock at the top
        cst_layout = QHBoxLayout()
        cst_label = QLabel("CST", self)
        cst_label.setStyleSheet("font-size: 20px;")

        self.cst_time = QLabel(self.get_time_by_zone("America/Chicago"), self)
        self.cst_time.setStyleSheet("font-size: 20px;")

        cst_layout.addWidget(cst_label)
        cst_layout.addWidget(self.cst_time)

        self.main_layout.addLayout(cst_layout)

        # Creating 6 more clocks under the CST clock
        self.time_labels = {}
        self.timezones = ["PST", "EST", "GMT", "CET", "IST", "JST"]
        for tz in self.timezones:
            tz_layout = QHBoxLayout()
            tz_label = QLabel(tz, self)
            tz_label.setStyleSheet("font-size: 16px;")

            self.time_labels[tz] = QLabel(self.get_time_by_zone(self.mapping.get(tz)), self)
            self.time_labels[tz].setStyleSheet("font-size: 16px;")

            tz_layout.addWidget(tz_label)
            tz_layout.addWidget(self.time_labels[tz])

            self.main_layout.addLayout(tz_layout)

        self.setLayout(self.main_layout)


    # This method updates the time for all clocks, every second, giving us live clock times.
    def update_times(self):
        self.cst_time.setText(self.get_time_by_zone("America/Chicago"))

        for tz in self.timezones:
            self.time_labels[tz].setText(self.get_time_by_zone(self.mapping.get(tz)))

    def start_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_times)
        self.timer.start(1000)

# Main method to run the application
if __name__ == "__main__":
    app = QApplication([])
    ex = WorldClockApp()
    ex.show()
    app.exec_()
