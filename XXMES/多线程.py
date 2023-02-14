from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5 import uic
#import threading
import sys,time

class  MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.ui=uic.loadUi(r'C:\2023工作\PyDev\XXMES\多线程.ui')
        #self.ui.resize(888,200) 
        self.thread={}
        self.ui.pushButton.clicked.connect(self.startWorker1)
        self.ui.pushButton_2.clicked.connect(self.startWorker2)
        self.ui.pushButton_3.clicked.connect(self.startWorker3)
        self.ui.pushButton_4.clicked.connect(self.endWorker1)
        self.ui.pushButton_5.clicked.connect(self.endWorker2)
        self.ui.pushButton_6.clicked.connect(self.endWorker3)
  
    def startWorker1(self):
        self.thread[1]=ThreadClass(parent=None,index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.myFunction)
        self.ui.pushButton.setEnabled(False)
    def startWorker2(self):
        self.thread[2]=ThreadClass(parent=None,index=2)
        self.thread[2].start()
        self.thread[2].any_signal.connect(self.myFunction)
        self.ui.pushButton_2.setEnabled(False)
    def startWorker3(self):
        self.thread[3]=ThreadClass(parent=None,index=3)
        self.thread[3].start()
        self.thread[3].any_signal.connect(self.myFunction)
        self.ui.pushButton_3.setEnabled(False)    
        
    def endWorker1(self):
        self.thread[1].stop()
        self.ui.pushButton.setEnabled(True)
    def endWorker2(self):
        self.thread[2].stop()
        self.ui.pushButton_2.setEnabled(True)
    def endWorker3(self):
        self.thread[3].stop()
        self.ui.pushButton_3.setEnabled(True)
        
    def myFunction(self,counter):
        cnt=counter
        index=self.sender().index
        if index==1:
            self.ui.progressBar.setValue(cnt)
        if index==2:
            self.ui.progressBar_2.setValue(cnt)
        if index==3:
            self.ui.progressBar_3.setValue(cnt)    
    
class ThreadClass(QtCore.QThread):
    any_signal=QtCore.pyqtSignal(int)    
    def __init__(self,parent=None,index=0):
        super(ThreadClass,self).__init__(parent)
        self.index=index
        self.isRunning=True
    def run(self):        
        print('Starting thread...',self.index)
        cnt=0
        while(True):
            cnt+=1
            if cnt==99:cnt=0
            time.sleep(0.01)
            self.any_signal.emit(cnt)
    def stop(self):
        self.isRunning=False
        print('Stopping thread...',self.index )
        self.terminate()
        
       
        
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=MyWindow()
    mainWindow.ui.show()  
    sys.exit(app.exec_())