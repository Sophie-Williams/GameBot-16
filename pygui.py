import pyautogui
import platform
import time

imageArray = ['play_hover.png','play.png', 'keep.png', 'keep_hover.png']
clicks = 0
x = 0
y = 0

myPlatform = platform.system()
print(pyautogui.size())

def findButtons():
	for i in imageArray:
		foundButton = pyautogui.locateCenterOnScreen(i)#, region=(1350,1500,950,350))
		if not foundButton is None: return (foundButton[0], foundButton[1])
	return(x,y)

def mouseClick(locX, locY):

	if myPlatform == "Darwin":
		pyautogui.click(locX/2, locY/2)
	else:
		pyautogui.click(locX, locY)

buttons = findButtons()
x, y = buttons
while True:
	if clicks > 0:
		buttons = findButtons()
		x, y = buttons
		clicks = 0
	if x > 0 and y> 0:
		mouseClick(x, y)
		clicks = clicks + 1
		print("Found it!")
	else:
		print("Not found")
	time.sleep(2)