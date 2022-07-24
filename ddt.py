import pyautogui
import time
import pyperclip

# 对于同一张截图校验有多少图片存在来判断状态

#pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159
def checkContains():
    for key,value in statueDict.items():
        statueDict[key] = pyautogui.locateCenterOnScreen(key,confidence=0.85)
    #     print(key,':',value,',',end='',flush=True)
    # print('',end='\r',flush=True)

def doAction():
    global statue
    global paiCount
    global currentTime
    # 开始，展开，确认需单击
    if statueDict['start.png'] != None:
        pyautogui.click(statueDict['start.png'].x,statueDict['start.png'].y,clicks=1,interval=0.2,duration=0.2,button="left")
        statue = 0
        paiCount = 0
        print('开始')
    if statueDict['unexpand.png'] != None:
        pyautogui.click(statueDict['unexpand.png'].x,statueDict['unexpand.png'].y,clicks=1,interval=0.2,duration=0.2,button="left")
        print('收缩道具栏')
    if statueDict['pai.png'] != None and paiCount < 3:
        pyautogui.click(statueDict['pai.png'].x,statueDict['pai.png'].y,clicks=1,interval=0.2,duration=0.2,button="left")
        paiCount += 1
        print('翻牌:',paiCount)
    if statueDict['confirm.png'] != None:
        pyautogui.click(statueDict['confirm.png'].x,statueDict['confirm.png'].y,clicks=1,interval=0.2,duration=0.2,button="left")
        print('花钱')
    # 角度+5，向右
    if statueDict['person.png'] != None and statue < 1:
        pyautogui.press(['up','up','up','up','up','right'],interval=0.1)
        print('调整角度')
    # 道具+发力
    if statueDict['person.png'] != None and statue < 2 and time.time()-currentTime>10:
        pyautogui.typewrite('33Z4B',interval=0.2)
        time.sleep(0.2)
        pyautogui.keyDown('space')
        time.sleep(2.5)
        pyautogui.keyUp('space')
        statue += 1
        print('打人')
        currentTime = time.time()


if __name__ == '__main__':
    # 创建图片存在状态字典,key为图片名,value为location
    statueDict = {'start.png':'','fly.png':'','unexpand.png':'','pai.png':'','person.png':'','pay.png':'','confirm.png':''}
    statue = 0
    paiCount = 0
    currentTime = time.time()

    while True:
        checkContains()
        doAction()

    # key=input('选择功能: 1.做一次 2.循环到死 \n')
    # if key=='1':
    #     #循环拿出每一行指令
    #     mainWork(sheet1)
    # elif key=='2':
    #     while True:
    #         mainWork(sheet1)
    #         time.sleep(0.1)
    #         print("等待0.1秒")
