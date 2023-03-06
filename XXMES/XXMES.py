from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5 import uic
import sys,time,threading 
import keyboard,mouse


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
        self.ui.resize(250,350)
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
        
        #可用角色控件
        self.adminLocate=self.ui.lineEdit_2
        self.sysAdminLocate=self.ui.lineEdit_3
        self.engLocate=self.ui.lineEdit_4
        self.engQLocate=self.ui.lineEdit_5
        self.execCount=self.ui.spinBox
        self.execUser=self.ui.pushButton_6
        self.engCheck=self.ui.checkBox
        self.engQCheck=self.ui.checkBox_2
        
        #指定角色位置
        self.adminLocate.setText('1347,304')
        self.sysAdminLocate.setText('1347,697')
        self.engLocate.setText('1347,728')
        self.engQLocate.setText('1347,760')
        self.execUser.clicked.connect(self.execUserBtn)
        
        #包含组件
        self.includeFrame=self.ui.frame_2
        self.includeTree=self.ui.treeView_2
        self.includeAddCTreeBtn=self.ui.pushButton_7
        self.includeAddTreeBtn=self.ui.pushButton_8
        self.includeCreateBtn=self.ui.pushButton_10
        self.includeDeleteBtn=self.ui.pushButton_11
        self.includeExecBtn=self.ui.pushButton_9
        root=QtGui.QStandardItem('父组件')
        self.model2=QtGui.QStandardItemModel(self)
        self.model2.appendRow(root)
        self.includeTree.setModel(self.model2)
         
        
        
        self.includeAddCTreeBtn.clicked.connect(self.includeAddCTreeCode)
        self.includeAddTreeBtn.clicked.connect(self.includeAddTreeCode)
        self.includeCreateBtn.clicked.connect(self.includeCreateCode)
        self.includeDeleteBtn.clicked.connect(self.includeDeleteCode)
        self.includeExecBtn.clicked.connect(self.includeExecCode)
        
        
        
                      
        self.log('软件正在启动...',2000)
        self.log_trade=threading.Thread(target=self.logTrade)
        self.log_trade.setDaemon(True)
        self.log_trade.start() 
        
        #成品组件——新建组件 	
        self.tree=self.ui.treeView            
        self.model=QtGui.QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(['组件树']) 
        root= QtGui.QStandardItem('父组件')
        self.model.appendRow(root)
        self.tree.setModel(self.model)
        self.tree.setStyle(QtWidgets. QStyleFactory.create('windows'))
        self.tree.setColumnWidth(0,220) 
        #self.tree.setColumnWidth(1,61) 
        
    
    #包含组件——生成C系树
    def includeAddCTreeCode(self):
        self.log('生成C系树')
        引擎结构.新建组件.includeAddCTreeCode(self)        
        
        
    #包含组件——生成轻奢树
    def includeAddTreeCode(self):
        self.log('生成轻奢树')
        引擎结构.新建组件.includeAddTreeCode(self)
    
    #包含组件——新建按钮
    def includeCreateCode(self):
        self.log('新建组件')
        引擎结构.新建组件.includeCreateCode(self)
        
    #包含组件——删除按钮
    def includeDeleteCode(self):
        self.log('删除组件')
        引擎结构.新建组件.includeDeleteCode(self)
    
    #包含组件——执行按钮
    def includeExecCode(self):
        self.log('执行包含组件')
        引擎结构.新建组件.includeExecCode(self)
        
       
    #可用角色——指定角色
    def execUserBtn(self):
        引擎结构.新建组件.execUserCode(self)
    
    #新建组件——生成树
    def CreateTreeBtn(self):
        pass
        引擎结构.新建组件.CreateTreeBtn(self)            
            
            
    #新建组件——添加子节点 
    def addTreeNodeBtn(self):
        引擎结构.新建组件.addTreeNodeBtn(self)         
    #新建组件——删除子节点
    def delTreeNodeBtn(self):
        引擎结构.新建组件.delTreeNodeBtn(self)
    #新建组件——定位控件
    def locTreeNodeBtn(self):
        引擎结构.新建组件.locTreeNodeBtn(self)    
    #新建组件——生成组件
    def execCreateNode(self):
        引擎结构.新建组件.execCreateNode(self)  
        #print(self.model.rowCount())  
        for index in range(self.model.rowCount()):
            item=self.model.item(index)            
            #print(item.text())            
            if item.hasChildren():
                for index in range(item.rowCount()):       
                    item2=item.child(index) 
                    self.execTreeCode(item,index,item2)                    
                    if item2.hasChildren():
                        for index in range(item2.rowCount()):
                            item3=item2.child(index)
                            #print(item3.text())
                            self.execTreeCode(item2,index,item3)
                            if item3.hasChildren():
                                for index in range(item3.rowCount()):
                                    item4=item3.child(index)
                                    #print(item4.text())
                                    self.execTreeCode(item3,index,item4)
        self.log('组件建立完毕')
                                    
    def execTreeCode(self,root,index,item):
        #轻奢00系          
        self.move(1706,316) 
        self.move(993,336) 
        keyboard.write(root.text())
                
        self.log('请手动点击组件组件位置')
        time.sleep(5) 
       # x,y=mouse.get_position()
        #mouse.click()         
       
        self.move(917,424) 
        keyboard.write(item.text(),0.1) 
        self.move(814,762)    
        self.move(749,907)   
        print(f'已建立组件：{item.text()}')
        
    def move(self,x,y,t=0.5):
        time.sleep(t)
        mouse.move(x,y)
        mouse.click()   
    
 
           
        
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