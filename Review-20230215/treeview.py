import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.ui=uic.loadUi(r'C:\2023工作\PyDev\Review-20230215\treeview.ui')
        self.createTreeBtn=self.ui.pushButton
        self.viewTreeBtn=self.ui.pushButton_2
        self.bar=QtWidgets.QStatusBar(self.ui.statusbar)
        self.createTreeBtn.clicked.connect(self.createTreeBtnCode)
        self.viewTreeBtn.clicked.connect(self.viewTreeBtnCode)
        
    def createTreeBtnCode(self):
        self.log('hi')
        pass
    
    def viewTreeBtnCode(self):
        app=QApplication.instance()
        app.exit()
        pass
    
    def log(self,message):
        self.bar.showMessage(message,3000)
    
    # 此处覆盖父类函数: 克服将鼠标放置于菜单栏上，状态栏就消失的问题；
    def event(self, QEvent):
        if QEvent.type() == QEvent.StatusTip:
            if QEvent.tip() == "":
                QEvent = QtCore. QStatusTipEvent("显示内容!")  # 此处为要始终显示的内容
        return super().event(QEvent)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MyWindow()
    window.ui.show()    
    sys.exit(app.exec_())


