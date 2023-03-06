import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5 import uic
import time

class StartTimer(QtCore.QThread):
    emitSignal=QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            self.emitSignal.emit(time.strftime('%H:%M:%S'))
            time.sleep(0.5)
            
    def stop(self):
        self.terminate()

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.ui=uic.loadUi(r'C:\2023工作\PyDev\XXMES\test\m.ui')
        startBtn=self.ui.pushButton
        stopBtn=self.ui.pushButton_2
        self.lcd=self.ui.lcdNumber
        
        startBtn.clicked.connect(self.startBtnCode)
        stopBtn.clicked.connect(self.stopBtnCode)
    def startBtnCode(self):
        self.timeThread=StartTimer()
        self.timeThread.emitSignal.connect(self.showTime)
        self.timeThread.start()
    def stopBtnCode(self):
        self.timeThread.stop()
    
    def showTime(self,t):
        self.lcd.display(t)
    
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MyWindow()
    window.ui.show()    
    sys.exit(app.exec_())