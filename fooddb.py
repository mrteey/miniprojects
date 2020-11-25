from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QListWidget, QTextEdit, QPushButton, QLineEdit, QFileDialog, QListWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from shutil import copyfile
import os

class faveMeal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Fave Meals')
        self.setFixedHeight(300)
        self.setFixedWidth(500)
        self.mainLayout = QHBoxLayout()
        self.foodLayout = QVBoxLayout()
        self.foodList = QListWidget()
        self.foodList.setFixedWidth(200)
        self.foodList.itemSelectionChanged.connect(self.showFood)
        self.summaryLayout = QVBoxLayout()
        self.addButton = QPushButton('Add Food')
        self.setLayout(self.mainLayout)
        self.mainLayout.addLayout(self.foodLayout)
        self.mainLayout.addLayout(self.summaryLayout)
        self.foodLayout.addWidget(self.addButton)
        self.foodLayout.addWidget(self.foodList)
        self.noimage = 'food/blank.png'
        self.image = QPixmap(self.noimage)
        self.label = QLabel()
        self.label.setPixmap(self.image)
        self.summary = QTextEdit('Select food to see summary')
        self.summary.setFixedHeight(200)
        self.summary.setReadOnly(True)
        self.summaryLayout.addWidget(self.label)
        self.summaryLayout.addWidget(self.summary)
        self.meals = {}
    
    def populate(self):
        self.foodList.clear()
        if self.meals:
            for m in self.meals:
                self.foodList.addItem(m.title())
        else:
            notification = QListWidgetItem('Add meals to see them here')
            notification.setFlags(Qt.NoItemFlags)
            self.foodList.addItem(notification)
    
    def showFood(self):
        try:
            food = self.foodList.currentItem().text().lower()
            image = self.meals.get(food).get('image')
            summary = self.meals.get(food).get('summary')
            self.image = QPixmap(image)
            self.label.setScaledContents(True)
            self.label.setPixmap(self.image)
            self.summary.setText(summary)
        except:
            pass
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            # Delete items on delete press
            food = self.foodList.currentItem().text()
            if food:
                self.meals.__delitem__(food.lower())
                self.label.setPixmap(QPixmap(self.noimage))
                self.summary.setText('Select food to see summary')
                self.populate()

class newFood(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Fave Meals')
        self.setFixedHeight(300)
        self.setFixedWidth(500)
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.food = QLineEdit()
        self.image = QPushButton('Select Image')
        self.imageFile = QLabel()
        self.summary = QTextEdit()
        self.buttonLayout = QHBoxLayout()
        self.saveButton = QPushButton('Save')
        self.cancelButton = QPushButton('Cancel')
        self.cancelButton.setStyleSheet('background:red')
        self.food.setPlaceholderText('Enter fave meal')
        self.mainLayout.addWidget(self.food)
        self.mainLayout.addWidget(self.image)
        self.mainLayout.addWidget(self.summary)
        self.mainLayout.addLayout(self.buttonLayout)
        self.buttonLayout.addWidget(self.saveButton)
        self.buttonLayout.addWidget(self.cancelButton)
        self.image.clicked.connect(self.selectImage)

    def selectImage(self):
        file_name = QFileDialog.getOpenFileName(self, "Select Image", "","Image (*.jpg *.png)")
        file_name = file_name[0]
        self.imageFile.setText(file_name)
        self.image.setText(file_name)

def add(favemeals, newfood, cancel=False):
    if favemeals.isVisible():
        favemeals.hide()
        newfood.show()
    else:
        if not cancel:
            food = newfood.food.text()
            summary = newfood.summary.toPlainText()
            image_src = newfood.imageFile.text() if newfood.imageFile.text() else 'food/default.jpg'
            image = os.path.join('food', os.path.basename(image_src))
            try:
                copyfile(image_src, image)
            except:
                pass
            favemeals.meals[food.lower()] = {'image':image, 'summary':summary}
            favemeals.populate()
        newfood.food.setText('')
        newfood.summary.setText('')
        newfood.image.setText('Select Image')
        newfood.hide()
        favemeals.show()


app = QApplication([])
favemeals = faveMeal()
newfood = newFood()
favemeals.populate()
favemeals.show()
favemeals.addButton.clicked.connect(lambda: add(favemeals, newfood))
newfood.saveButton.clicked.connect(lambda: add(favemeals, newfood))
newfood.cancelButton.clicked.connect(lambda: add(favemeals, newfood, True))
app.exec_()