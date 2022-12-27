from PyQt5 import QtWidgets
import qdarkstyle

from main_controller import controller

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    window = controller()
    window.show()
    sys.exit(app.exec_())