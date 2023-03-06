import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
        
    def init_ui(self):
        self.ui=uic.loadUi(r'C:\2023工作\PyDev\Review-20230215\review.ui')
        """
        self.bar=QtWidgets.QStatusBar(self.ui.statusbar) 
        self.appendBtn=QtWidgets.QPushButton(self.ui.pushButton)
        self.modifyBtn=QtWidgets.QPushButton(self.ui.pushButton_2)
        self.nextBtn=QtWidgets.QPushButton(self.ui.pushButton_3)
        self.delayTimeEdit=QtWidgets.QSpinBox(self.ui.spinBox)
        self.autoCheckBox=QtWidgets.QCheckBox(self.ui.checkBox)
        self.nextTimeEdit=QtWidgets.QSpinBox(self.ui.spinBox_2)
        """
        
    def appendBtnCode(self):
        self.log('添加内容')
        
    def modifyBtnCode(self):
        self.log('修改内容')
            
    def nextBtnCode(self):
        self.log('开始复习',3000)
        
    def autoCheckBoxCode(self):
        self.log('自动复习')
    
 
    def log(self,message):
        self.bar.showMessage(message,3000)
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MyWindow()
    window.ui.show()    
    sys.exit(app.exec_())


