import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Controle(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        pass
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Controle()
    sys.exit(app.exec_())
