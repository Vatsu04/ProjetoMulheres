import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tela_de_resumos(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.show()
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Tela_de_resumos()
    sys.exit(app.exec_())
