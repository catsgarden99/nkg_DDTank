import pyautogui
import time
import xlrd
import pyperclip

# 对于同一张截图校验有多少图片存在来判断状态

#定义鼠标事件

#pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159

def mouseClick(clickTimes,lOrR,img,reTry):
    if reTry == 1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                break
            print("未找到匹配图片,0.1秒后重试")
            time.sleep(0.1)
    elif reTry == -1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
            time.sleep(0.1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                print("重复")
                i += 1
            time.sleep(0.1)

def checkContains():
    for value in statueDict.keys():
        statueDict[value] = pyautogui.locateCenterOnScreen(img,confidence=0.9)

if __name__ == '__main__':
    # 创建图片存在状态字典,key为图片名,value为location
    statueDict = {'run.png':'None','start.png':'None','fly.png':'None'}

    checkContains(statueDict)

    key=input('选择功能: 1.做一次 2.循环到死 \n')
    if key=='1':
        #循环拿出每一行指令
        mainWork(sheet1)
    elif key=='2':
        while True:
            mainWork(sheet1)
            time.sleep(0.1)
            print("等待0.1秒")
