import pyautogui
import time

time.sleep(3)

# Windows计算器的按钮截图
five = 'seguir.png'
eight = '8.png'
multiply = 'multiply.png'
equals = 'equals.png'

# 图片识别和点击的函数


def find_and_click(image):
    d = pyautogui.locateCenterOnScreen(image,confidence=0.9)
    try:
    	x = d[0];
    	y = d[1];
    	pyautogui.moveTo(600,300,duration=0.5)
    	time.sleep(1)
    	pyautogui.click(x,y)
    	time.sleep(1)
    	pyautogui.moveTo(600,300,duration=0.5)

    except:
    	print("Kuek")
    	pyautogui.press('f5')
    	time.sleep(5)


# 执行5*8=
#find_and_click(five)
#find_and_click(multiply)
#find_and_click(eight)
#find_and_click(equals)
for i in range(1000000):
    #time.sleep(0.5)
    #pyautogui.doubleClick()
    find_and_click(five)
    time.sleep(1)
    pyautogui.scroll(-25)
    time.sleep(15)
    #pyautogui.press('down')
    #pyautogui.press('down')
