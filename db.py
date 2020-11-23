from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QListWidget, QTextEdit, QPushButton, QLineEdit, QFileDialog
from PyQt5.QtGui import QPixmap
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
        self.foodList.itemSelectionChanged.connect(self.showFood)
        self.summaryLayout = QVBoxLayout()
        self.addButton = QPushButton('Add Food')
        self.setLayout(self.mainLayout)
        self.mainLayout.addLayout(self.foodLayout)
        self.mainLayout.addLayout(self.summaryLayout)
        self.foodLayout.addWidget(self.addButton)
        self.foodLayout.addWidget(self.foodList)
        self.image = QPixmap('food/default.jpg')
        self.label = QLabel('default')
        self.label.setPixmap(self.image)
        self.summary = QTextEdit('Select food to see summary')
        self.summary.setReadOnly(True)
        self.summaryLayout.addWidget(self.label)
        self.summaryLayout.addWidget(self.summary)
        self.meals = {'tuwo':{'image':'food/tuwo.jpg', 'summary':"Tuwon shinkafa is a type of Nigerian and Niger dish from Niger and the northern part of Nigeria. It is a thick pudding prepared from a local rice or Maize or millet that is soft and sticky, and is usually served with different types of soups like Miyan kuka, Miyan kubewa, Miyan taushe."}}
    
    def populate(self):
        self.foodList.clear()
        for m in self.meals:
            self.foodList.addItem(m.title())
    
    def showFood(self):
        food = self.foodList.currentItem().text().lower()
        image = self.meals.get(food).get('image')
        summary = self.meals.get(food).get('summary')
        self.image = QPixmap(image)
        self.label.setPixmap(self.image)
        self.summary.setText(summary)

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
        _file = QFileDialog.getOpenFileUrl(self, "Select Image")
        # self.imageFile.setText()
        # print(imageSelector.getExistingDirectory())
        # print(imageSelector.getOpenFileUrl)
        new_file = str(_file).replace("(PyQt5.QtCore.QUrl('", '').replace("'), 'All Files (*)')", '')
        print(new_file)
        filename = os.path.basename(new_file)
        copyfile(new_file, 'food/'+filename)

def add(favemeals, newfood, cancel=False):
    if favemeals.isVisible():
        favemeals.hide()
        newfood.show()
    else:
        if not cancel:
            food = newfood.food.text()
            summary = newfood.summary.toPlainText()
            image = 'food/default.jpg'
            favemeals.meals[food.lower()] = {'image':image, 'summary':summary}
            favemeals.populate()
        newfood.food.setText('')
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