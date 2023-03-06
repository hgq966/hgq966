"""
XXMES-引擎结构-新建组件
浙江·武义·熊熊
20230211
"""
from PyQt5 import QtCore,QtWidgets,QtGui
import keyboard,mouse 
import time,threading

 
#生成树
def CreateTreeBtn(self):
    pass
    self.treeviewFrame.setEnabled(False)
    if self.treeviewSeriesName.text().strip()=="":
        self.log('系列名称为空')
        self.treeviewFrame.setEnabled(True)
    else:
        self.log('开始生成树',5000)
        seriesRootName=self.treeviewSeriesName.text().strip()
        series={
            0:['单门','子母','双开','三开','边固四开子母','边固四开'],
            1:['子母','连体子母'],
            2:['边固四开子母','四开子母','边固立柱四开子母'],
            3:['边固立柱四开子母','立柱四开子母'],
            4:['边固四开','四开','边固立柱四开'],
            5:['边固立柱四开','立柱四开'] }
        for index,name in series.items():
            #print(index,'-->',name)
            self.tree.setFocus()
            if index==0:
                self.model.setItem(0,0,QtGui.QStandardItem(seriesRootName))
                self.tree.repaint()
                time.sleep(0.3)
                index=self.tree.currentIndex()
                root=self.model.itemFromIndex(index)                     
                for subItem in name:                        
                    root.appendRow(QtGui.QStandardItem(subItem+seriesRootName))
                    self.tree.expandAll()
                    self.tree.repaint()
                    time.sleep(0.15)
            else:
                root=self.model.findItems(name[0]+seriesRootName, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)                    
                for subItem in name[1:len(name)]:
                    print('0-->',subItem+seriesRootName)
                    root[0].appendRow(QtGui.QStandardItem(subItem+seriesRootName))
                    self.tree.expandAll()
                    self.tree.repaint()
                    time.sleep(0.15)
        self.log('就绪...')
        self.treeviewFrame.setEnabled(True)     
    
#添加子节点 
def addTreeNodeBtn(self):
    index=self.tree.currentIndex()        
    if not index.isValid(): 
        self.log('没有选择组件')
        return
    root=self.tree.model().itemFromIndex(index) 
    node = QtGui.QStandardItem('子组件')
    root.appendRow(node) 
    self.tree.expandAll()
    index=self.tree.currentIndex()
    self.log('添加新组件')
    
#删除子节点
def delTreeNodeBtn(self):
    index=self.tree.currentIndex()        
    if not index.isValid(): 
        self.log('没有选择组件')
        return
    parent=index.parent()   
    item=self.model.itemFromIndex(index)
    if parent.row()==-1:
        self.log('不能删除根组件')
    else:
        item.parent().removeRow(index.row())
        self.log('删除子组件')

#设置鼠标位置
def setTreeviewMouseLocate(self,x,y):
    pass
    self.MOUSE_LOCATE=(0,0)
    if self.treeviewLocBtn.isEnabled()==False:
        index=self.tree.currentIndex()
        parent=index.parent()   
        item=self.model.itemFromIndex(index)     
        self.log(f'指定 {item.text()} 位置') 
        time.sleep(0.1)
        print(parent.row())
        if parent.row()==-1:
            print('设置根节点')
            self.model.setItem(index.row(),1,QtGui.QStandardItem(f"{x},{y}"))
            time.sleep(0.1)
        else:
            print('设置子节点')
            item.parent().setChild(index.row(),1,QtGui.QStandardItem(f"{x},{y}"))
            time.sleep(0.1)
        #self.tree.setFocus()
        #self.tree.repaint()
        #time.sleep(0.25)
        self.treeviewLocBtn.setEnabled(True)
   
def printMousePosition():   
    x,y=mouse.get_position()
    program.mouseLocateTrigger.emit(program,x,y)
    

#指定位置
def locTreeNodeBtn(self):    
    global program
    program=self
    self.treeviewLocBtn.setEnabled(False)
    index=self.tree.currentIndex()
    if not index.isValid(): 
        self.log('没有选择组件')
        self.treeviewLocBtn.setEnabled(True)
        return     
    print('开始注册热键')  
    #k.clear_all_hotkeys()
    try:
        
        time.sleep(0.1)
        keyboard.add_hotkey('ctrl',callback=printMousePosition,suppress = False)
        time.sleep(0.1)
        #k.wait('esc')
    except:
        self.log('热键注册失败，请重试',3000)
        return
    else:
        self.log('已注册热键,Ctrl 指定组件位置',3000)
        
    

 
    
    
        
#生成组件
def execCreateNode(self):
    pass
    return

    
#指定角色
def execUserCode(self):
    self.log('开始指定角色')
    time.sleep(0.5)
    self.log('请在2秒内指定 可用角色 位置')
    z=69
    xx=0
    time.sleep(2)
    for i in range(self.execCount.value()):
        x,y=mouse.get_position()
        xx,yy=x,y
        mouse.click()
        x,y=self.adminLocate.text().split(',',1)
        x,y=int(x),int(y)
        move(x,y)
        x,y=self.sysAdminLocate.text().split(',',1)
        x,y=int(x),int(y)
        move(x,y)
        if self.engCheck.isChecked():
            x,y=self.engLocate.text().split(',',1)
            x,y=int(x),int(y)
            move(x,y)
        if self.engQCheck.isChecked():
            x,y=self.engQLocate.text().split(',',1)
            x,y=int(x),int(y)
            move(x,y)
        move(1525,486)    
        move(1855,1014)
        x,y=mouse.get_position()
        mouse.move(xx,yy+z)
        time.sleep(1)
        #移动鼠标
        
    
def move(x,y,t=0.5):
        time.sleep(t)
        mouse.move(x,y)
        mouse.click()    

#包含组件——生成C系树
def includeAddCTreeCode(self):
    self.log('生成C系树')
    self.includeFrame.setEnabled(False)
    #treeIn=  QtWidgets.QTreeView(self.includeTree)
    modelIn= QtGui.QStandardItemModel(self)
    treeIn=self.includeTree     
    
    root=QtGui.QStandardItem('父组件')
    modelIn.appendRow(root)
    treeIn.setModel(modelIn)
    
    
    series={
            0:['单门','子母','连体子母','双开','三开','边固四开子母','四开子母','边固立柱四开子母','立柱四开子母','边固四开','四开','边固立柱四开','立柱四开'],
            1:['单门','单层单门'],
            2:['子母','单层子母','93铝制子外','93铝制子内'],
            3:['连体子母','单层连体子母'],
            4:['双开','单层双开','93铝制副外','93铝制副内'],
            5:['三开','单层三开'],
            6:['边固四开子母','单层边固四开子母','93铝制副外','93铝制副内','边子外','边子内'],
            7:['四开子母','单层四开子母'],
            8:['边固立柱四开子母','单层边固立柱四开子母'],
            9:['立柱四开子母','单层立柱四开子母'],
            10:['边固四开','单层边固四开','93铝制副外','93铝制副内','边门外','边门内'],
            11:['四开','单层四开'],
            12:['边固立柱四开','单层边固立柱四开'],
            13:['立柱四开','单层立柱四开']
             }
    for index,name in series.items():
        #print(index,'-->',name)
        treeIn.setFocus()
        if index==0:
            #self.model.setItem(0,0,QtGui.QStandardItem(seriesRootName))
            treeIn.repaint()
            time.sleep(0.3)
            index=treeIn.currentIndex()
            root=modelIn.itemFromIndex(index)  
            root.appendRow(QtGui.QStandardItem('93铝制主外'))                   
            root.appendRow(QtGui.QStandardItem('93铝制主内'))                   
            for subItem in name:                        
                root.appendRow(QtGui.QStandardItem(subItem))
                treeIn.expandAll()
                treeIn.repaint()
                time.sleep(0.1)
        else:
            root=modelIn.findItems(name[0], QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)                    
            for subItem in name[1:len(name)]:
                print('0-->',subItem)
                root[0].appendRow(QtGui.QStandardItem(subItem))
                treeIn.expandAll()
                treeIn.repaint()
                time.sleep(0.1)
    self.log('就绪...')
    self.includeFrame.setEnabled(True) 

#包含组件——生成轻奢树
def includeAddTreeCode(self):
    self.log('生成轻奢树')
    self.includeFrame.setEnabled(False)
    #treeIn=  QtWidgets.QTreeView(self.includeTree)
    modelIn= QtGui.QStandardItemModel(self)
    treeIn=self.includeTree     
    
    root=QtGui.QStandardItem('父组件')
    modelIn.appendRow(root)
    treeIn.setModel(modelIn)    
    
    series={
            0:['单门','子母','连体子母','双开','三开','边固四开子母','四开子母','边固立柱四开子母','立柱四开子母','边固四开','四开','边固立柱四开','立柱四开'],
            1:['单门','单层单门'],
            2:['子母','单层子母','模压子外录单','模压子内录单'],
            3:['连体子母','单层连体子母'],
            4:['双开','单层双开','模压副外录单','模压副内录单'],
            5:['三开','单层三开'],
            6:['边固四开子母','单层边固四开子母','模压副外录单','模压副内录单','模压边子外录单','模压边子内录单'],
            7:['四开子母','单层四开子母'],
            8:['边固立柱四开子母','单层边固立柱四开子母'],
            9:['立柱四开子母','单层立柱四开子母'],
            10:['边固四开','单层边固四开','模压副外录单','模压副内录单','模压边门外录单','模压边门内录单'],
            11:['四开','单层四开'],
            12:['边固立柱四开','单层边固立柱四开'],
            13:['立柱四开','单层立柱四开']
             }
    for index,name in series.items():
        #print(index,'-->',name)
        treeIn.setFocus()
        if index==0:
            #self.model.setItem(0,0,QtGui.QStandardItem(seriesRootName))
            treeIn.repaint()
            time.sleep(0.3)
            index=treeIn.currentIndex()
            root=modelIn.itemFromIndex(index)  
            root.appendRow(QtGui.QStandardItem('主外录单'))                   
            root.appendRow(QtGui.QStandardItem('主内录单'))                   
            for subItem in name:                        
                root.appendRow(QtGui.QStandardItem(subItem))
                treeIn.expandAll()
                treeIn.repaint()
                time.sleep(0.1)
        else:
            root=modelIn.findItems(name[0], QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)                    
            for subItem in name[1:len(name)]:
                print('0-->',subItem)
                root[0].appendRow(QtGui.QStandardItem(subItem))
                treeIn.expandAll()
                treeIn.repaint()
                time.sleep(0.1)
    self.log('就绪...')
    self.includeFrame.setEnabled(True) 

#包含组件——新建按钮
def includeCreateCode(self):
    self.log('新建组件')
    index=self.includeTree.currentIndex()        
    if not index.isValid(): 
        self.log('没有选择组件')
        return
    root=self.includeTree.model().itemFromIndex(index) 
    node = QtGui.QStandardItem('子组件')
    root.appendRow(node) 
    self.includeTree.expandAll()
    #index=self.tree.currentIndex()
    self.log('添加新组件')
    
 
#包含组件——删除按钮
def includeDeleteCode(self):
    self.log('删除组件')
    index=self.includeTree.currentIndex()        
    if not index.isValid(): 
        self.log('没有选择组件')
        return
    parent=index.parent()   
    item=self.includeTree.model().itemFromIndex(index)
    if parent.row()==-1:
        self.log('不能删除根组件')
    else:
        item.parent().removeRow(index.row())
        self.log('删除子组件')
        
        
#包含组件——执行按钮
def includeExecCode(self):
    self.log('执行包含组件')
    self.includeFrame.setEnabled(False)
    #treeIn=  QtWidgets.QTreeView(self.includeTree)
     
    treeIn=self.includeTree 
    modelIn=treeIn.model()  
    index=treeIn.currentIndex()  
    if not index.isValid(): 
        self.log('没有选择组件')
        self.includeFrame.setEnabled(True)
        return       
    item=modelIn.itemFromIndex(index)     
    if item.hasChildren():
        self.log('有子组件')
        self.log('请在2秒内定位到 包含组件 位置')
        time.sleep(2.5)
        mouse.click()                
        move(1682,203)
        move(970,311)
        for index in range(item.rowCount()):
            item2=item.child(index)
            if not item2.hasChildren():                
                keyboard.write(item2.text(),delay=0.05)
                time.sleep(6)
        #move(938,244)
        #move(1162,375) #确定按钮
        #move(1085,210)
        self.includeFrame.setEnabled(True)       
                
                
    else:
        self.log('没有子组件')
        
        
    self.includeFrame.setEnabled(True)
