"""
XXMES-引擎结构-新建组件
浙江·武义·熊熊
20230211
"""
from PyQt5 import QtCore,QtWidgets,QtGui
import keyboard as k
import mouse as m
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
                    time.sleep(0.25)
            else:
                root=self.model.findItems(name[0]+seriesRootName, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)                    
                for subItem in name[1:len(name)]:
                    print('0-->',subItem+seriesRootName)
                    root[0].appendRow(QtGui.QStandardItem(subItem+seriesRootName))
                    self.tree.expandAll()
                    self.tree.repaint()
                    time.sleep(0.25)
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
    x,y=m.get_position()
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
        k.add_hotkey('ctrl',callback=printMousePosition,suppress = False)
        time.sleep(0.1)
        #k.wait('esc')
    except:
        self.log('热键注册失败，请重试',3000)
        return
    else:
        self.log('已注册热键,Ctrl 指定组件位置',3000)
        
    

 
    
    
        
#生成组件
def execCreateNode(self):
    index=self.tree.currentIndex()        
    if not index.isValid():
        self.log('没有选择组件')
        return
    self.log('执行新建组件') 
    print(self.model.itemFromIndex(self.tree.currentIndex()).text())