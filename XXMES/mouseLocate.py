"""
鼠标位置记录
按Ctrl记录当前鼠标位置
按Esc退出程序
郝广卿——浙江·熊熊安防·20230205
"""
import keyboard  
import mouse  
import time
i=1
"""
time.sleep(2)
z=69
for i  in range(1,11):
    x,y=mouse.get_position()
    mouse.move(x,y+z)
    time.sleep(0.3)
exit()
"""
def printMousePosition():
    global i
    print(f"{i}-->{mouse.get_position()}")
    i+=1

keyboard.add_hotkey('ctrl',callback= printMousePosition)
keyboard.wait('esc')