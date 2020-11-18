from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtCore import Qt
import requests

app = QApplication([])

class Weather(QWidget):
    def __init__(self):
        super().__init__()
        self.apiKey = 'bf527f2c0ece63f0e185788e4ea21be3'
        self.base_url = 'https://api.openweathermap.org/data/2.5'
        self.setWindowTitle('Weather App')
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        self.mainLayout = QVBoxLayout()
        self.setStyleSheet('background-color:black;')
        self.setLayout(self.mainLayout)
        self.textField = QLineEdit()
        self.textField.setPlaceholderText('Enter city name')
        self.textField.setStyleSheet('color:#fff;')
        self.submitButton = QPushButton('Submit')
        self.submitButton.setStyleSheet('background-color:#fff; color:#000')
        self.submitButton.clicked.connect(self.get_weather)
        self.resultField = QLabel()
        self.mainLayout.addWidget(self.textField)
        self.mainLayout.addWidget(self.submitButton)
        self.mainLayout.addWidget(self.resultField)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.get_weather()

    def get_weather(self):
        city = self.textField.text().title()
        try:
            response = requests.get(f'{self.base_url}/weather?q={city}&appid={self.apiKey}')
            result = response.json()
            self.resultField.setStyleSheet('color:#fff;')
            self.resultField.setText(f"The weather information for {city}: \n Country: {result.get('sys').get('country')} \n Longitude: {result.get('coord').get('lon')} \n Latitude: {result.get('coord').get('lat')} \n Temperature: {round(result.get('main').get('temp')-273)}c \n Condition: {result.get('weather')[0].get('description')}")
            self.textField.setText('')
        except Exception as e:
            print(e)
            self.resultField.setStyleSheet('color:red;')
            self.resultField.setText(f'Opps!\nWe could not get weather information\nfor {city} at the moment')

window = Weather()
window.show()
app.exec_()


