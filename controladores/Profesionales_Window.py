from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
class Profesionales_Window(QMainWindow):
    def __init__(self, parent=None):
        super(Profesionales_Window, self).__init__(parent)
        loadUi('./archivos_ui/Profesionales.ui',self)
        #self.setupUi(self)

    def cargarDatos(self):
        pass


