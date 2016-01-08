import pyautogui
import time

imageArray = ['play_hover.png','play.png', 'keep.png', 'keep_hover.png']
clicks = 0
x = 0
y = 0

def findButtons():
	for i in imageArray:
		foundButton = pyautogui.locateCenterOnScreen(i, region=(1350,1500,950,350))
		if not foundButton is None: return (foundButton[0], foundButton[1])
	return(x,y)

buttons = findButtons()
x, y = buttons
while True:
	if clicks > 20:
		buttons = findButtons()
		x, y = buttons
		clicks = 0
	if x > 0 and y> 0:
		pyautogui.click(x/2, y/2)
		pyautogui.click(x/2, y/2)
		clicks = clicks + 1
	time.sleep(2)