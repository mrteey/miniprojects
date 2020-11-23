from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from sandc import Sandc

states = Sandc()

class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color:white; color:black')
        self.setWindowTitle('Game')
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        self.mainLayout = QVBoxLayout()
        self.questionLayout = QVBoxLayout()
        self.resultLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.questionLayout)
        self.mainLayout.addLayout(self.resultLayout)
        self.setLayout(self.mainLayout)
        self.question = QLabel()
        self.state = ''
        self.capital = ''
        self.result = QLabel('No question answered yet!')
        self.score = QLabel('Score: 0')
        self.answer = QLineEdit()
        self.answer.setPlaceholderText('Enter your answer here')
        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.submit)
        self.submitButton.setStyleSheet('background-color:black; color:white')
        self.questionLayout.addWidget(self.question)
        self.questionLayout.addWidget(self.answer)
        self.questionLayout.addWidget(self.submitButton)
        self.resultLayout.addWidget(self.score)
        self.resultLayout.addWidget(self.result)
        
    def start(self):
        self.answer.setText('')
        _state = states.get_state()
        state = _state.get('state')
        capital = _state.get('capital')
        self.question.setText(f'What is the capital of {state}?')
        self.state = state
        self.capital = capital
        return _state
    
    def submit(self):
        score = int(self.score.text().split()[-1])
        if self.capital.lower() == self.answer.text().lower():
            score+=1
            self.score.setText(f'Score: {score}')
            self.result.setText('Thats correct!')
            return self.start()
        score-=1
        self.score.setText(f'Score: {score}')
        self.result.setText(f'Opps incorrect!\nThe capital of {self.state}\nis {self.capital}\nnot {self.answer.text()}')
        return self.start()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.submit()

app = QApplication([])
window = Game()
window.start()
window.show()
app.exec_()