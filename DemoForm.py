# DemoForm.py
# DemoFrom.ui(디자인단) + DemoFrom.py(로직단)
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

# 디자인 파일 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

# 폼클래스 정의
class DemoForm(QDialog, form_class):
    # 초기화 method
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt 데모")

#진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()