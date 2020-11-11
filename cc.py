# initial a project folder
# run python -m venv venv
# run venv/Scripts/activate
# run pip install PyQt5

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
currencyFrom.addItems(['NGN (₦)', 'USD ($)'])
currencyTo = QComboBox()
currencyTo.setMinimumHeight(30)
currencyTo.setMinimumWidth(100)
currencyTo.addItems(['USD ($)', 'NGN (₦)' ])
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

def _convert(amount, _from, to):
    if '$' in _from:
        if '₦' in to:
            if amount.isdigit():
                result.setText(f'${amount} equals to ₦{int(amount)*400}')
            else:
                result.setText('0')
        else:
            result.setText(amount)
    else:
        if '$' in to:
            if amount.isdigit():
                result.setText(f'₦{amount} equals to ${int(amount)/400}')
            else:
                result.setText('0')
        else:
            result.setText(amount)
button.clicked.connect(lambda: _convert(amount.toPlainText(), currencyFrom.currentText(), currencyTo.currentText()))
mainWindow.show()
app.exec_()