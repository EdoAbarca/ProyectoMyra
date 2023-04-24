from PyQt5.QtWidgets import *
from controladores.Profesionales_Window import Profesionales_Window
import sys
from PyQt5.QtGui import *

def main():
    app = QApplication(sys.argv)
    form = Profesionales_Window()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()