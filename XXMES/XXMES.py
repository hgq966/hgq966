from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5 import uic
import sys,time,threading,keyboard
import  引擎结构.新建组件 



class  MyWindow(QtWidgets.QMainWindow):
    mouseLocateTrigger=QtCore.pyqtSignal(object,int,int)
    def __init__(self):
        super().__init__()
        self.init_ui()  
        
        
    def init_ui(self):
        #载入窗体
        self.ui=uic.loadUi(r'C:\2023工作\PyDev\XXMES\引擎结构-20230209.ui') 
        
        #设置label图片
        self.ui.resize(200,350)
        self.ui.label.setPixmap(QtGui.QPixmap(r'C:\2023工作\PyDev\XXMES\background.jpg'))     
        self.ui.horizontalSlider.valueChanged.connect(self.setOpacity)
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        
        #连接控件 
        self.treeviewFrame=self.ui.frame
        self.treeviewSeriesName=self.ui.lineEdit    #系列名称
        self.treeviewCreateTree=self.ui.pushButton_5       #生成树
        self.treeviewNewNodeBtn=self.ui.pushButton_2    #新建节点
        self.treeviewDelNodeBtn=self.ui.pushButton      #删除节点
        self.treeviewExecBtn=self.ui.pushButton_3       #生成组件
        self.treeviewLocBtn=self.ui.pushButton_4       #指定位置
        
        self.treeviewCreateTree.clicked.connect(self.CreateTreeBtn)     
        self.treeviewNewNodeBtn.clicked.connect(self.addTreeNodeBtn)
        self.treeviewDelNodeBtn.clicked.connect(self.delTreeNodeBtn)
        self.treeviewLocBtn.clicked.connect(self.locTreeNodeBtn)
        self.treeviewExecBtn.clicked.connect(self.execCreateNode)        
        self.mouseLocateTrigger.connect(引擎结构.新建组件.setTreeviewMouseLocate)
        
                      
        self.log('软件正在启动...',2000)
        self.log_trade=threading.Thread(target=self.logTrade)
        self.log_trade.setDaemon(True)
        self.log_trade.start() 
        
        #成品组件——新建组件 	
        self.tree=self.ui.treeView            
        self.model=QtGui.QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(['组件树','位置']) 
        root= QtGui.QStandardItem('父组件')
        self.model.appendRow(root)
        self.tree.setModel(self.model)
        self.tree.setStyle(QtWidgets. QStyleFactory.create('windows'))
        self.tree.setColumnWidth(0,150) 
        self.tree.setColumnWidth(1,50) 
        print('开始注册热键') 
        try:        
            time.sleep(0.1)
           # keyboard.add_hotkey('ctrl',callback=引擎结构.新建组件.printMousePosition,suppress = False)
            time.sleep(0.1)
            #k.wait('esc')
        except:
            self.log('热键注册失败，请重试',3000)
            return
        else:
            self.log('已注册热键,Ctrl 指定组件位置',3000)
    
    #生成树
    def CreateTreeBtn(self):
        pass
        引擎结构.新建组件.CreateTreeBtn(self)            
            
            
    #添加子节点 
    def addTreeNodeBtn(self):
        引擎结构.新建组件.addTreeNodeBtn(self)   
        
    #删除子节点
    def delTreeNodeBtn(self):
        引擎结构.新建组件.delTreeNodeBtn(self)
    #定位控件
    def locTreeNodeBtn(self):
        引擎结构.新建组件.locTreeNodeBtn(self)    
    #生成组件
    def execCreateNode(self):
        引擎结构.新建组件.execCreateNode(self)     
        
           
        
    #状态栏常驻文本
    def logTrade(self):        
        while True:
            if self.ui.statusbar.currentMessage()=="":
                self.ui.statusbar.showMessage('就绪...')
                time.sleep(1)   
                    
    #状态栏文本                
    def log(self,str,t=1200):
        #状态栏显示文本         
        print(str)
        self.ui.statusbar.showMessage(str,t)       
        #self.ui.statusbar.clearMessage()
        
    #设置窗体透明度
    def setOpacity(self):
        print(f'设置窗体透明度为：{self.ui.horizontalSlider.value()} %')
        self.ui.setWindowOpacity(self.ui.horizontalSlider.value()/100)

 
        
     
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)    
    window=MyWindow()
    window.ui.show()
    sys.exit(app.exec_())