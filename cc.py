# initial a project folder
# run python -m venv venv
# run venv/Scripts/activate
# run pip install PyQt5

import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QComboBox

app = QApplication([])
mainWindow = QWidget()
mainWindow.setStyleSheet('background-color:white; color:black')
mainWindow.setWindowTitle('Currency Converter')
container = QVBoxLayout()
mainWindow.setLayout(container)
inputs = QWidget()
labels = QWidget()
inputsLayout = QHBoxLayout()
labelsLayout = QHBoxLayout()
inputs.setLayout(inputsLayout)
labels.setLayout(labelsLayout)
amountLabel = QLabel('Amount')
amountLabel.setStyleSheet('color:red')
fromLabel = QLabel('From')
fromLabel.setStyleSheet('color:red')
toLabel = QLabel('To')
toLabel.setStyleSheet('color:red')
amount = QTextEdit('10')
amount.setMaximumHeight(30)
amount.setMaximumWidth(100)
currencyFrom = QComboBox()
currencyFrom.setMinimumHeight(30)
currencyFrom.setMinimumWidth(100)
currencyFrom.addItems(['NGN (₦)', 'USD ($)', 'EURO (€)', 'POUND (£)', 'YEN (¥)'])
currencyTo = QComboBox()
currencyTo.setMinimumHeight(30)
currencyTo.setMinimumWidth(100)
currencyTo.addItems(['NGN (₦)', 'USD ($)', 'EURO (€)', 'POUND (£)', 'YEN (¥)'])
inputsLayout.addWidget(amount)
inputsLayout.addWidget(currencyFrom)
inputsLayout.addWidget(currencyTo)
labelsLayout.addWidget(amountLabel)
labelsLayout.addWidget(fromLabel)
labelsLayout.addWidget(toLabel)
button = QPushButton('Convert')
button.setStyleSheet('background-color:red; color:white')
result = QLabel('$300 is equivalent to ₦1200')
container.addWidget(labels)
container.addWidget(inputs)
container.addWidget(button)
container.addWidget(result)

def convert_offline(amount, _from, to):
    _from = _from.split('(')[-1][0]
    to = to.split('(')[-1][0]
    amount = int(amount) if amount.isdigit() else 1
    conversions = {'$':
                        {'₦':380, '€':140, '£':0.12, '$':1, '¥':0.034}, 
                    '₦':
                        {'$':0.0026, '€':0.00076, '£':0.00026, '₦':1, '¥':0.44},
                    '£':
                        {'$':112, '€':210, '₦':450, '£':1, '¥':0.74},
                    '€':
                        {'$':150, '£':15, '₦':550, '€':1, '¥':0.34},
                    '¥':
                        {'$':70, '£':30, '₦':89, '€':95, '¥':1}
                    }
    rate = conversions.get(_from).get(to)
    value = rate*amount
    result.setText(f'{_from}{amount} equals to {to}{value}')
    return value

def convert_online(amount, _from, to):
    apikey = '20b9a28a6a37cdb1ff95'
    _from = _from.split('(')[0]
    to = to.split('(')[0]
    amount = int(amount) if amount.isdigit() else 1
    url = f'https://free.currconv.com/api/v7/convert?q={_from.strip()}_{to.strip()}&compact=ultra&apiKey={apikey}'
    print(url)
    r = requests.get(url)
    rate = list(r.json().values())[0]
    value = rate*amount
    result.setText(f'{_from}{amount} equals to {to}{value}')

def get_converter(amount, _from, to):
    try:
        return convert_online(amount, _from, to)
    except:
        return convert_offline(amount, _from, to)

button.clicked.connect(lambda: get_converter(amount.toPlainText(), currencyFrom.currentText(), currencyTo.currentText()))
mainWindow.show()
app.exec_()