import time
from multiprocessing import get_context
from multiprocessing import Pool
from mss import mss
from PIL import Image
from pynput.keyboard import Controller
import time

keyboard = Controller()

current = [1,2,3,4]

def watch(current):
	toggle = False
	if current == 1:
		scan1 = mss()
		time.sleep(current/4)
		print("First point activated")
		while True:
			above_scan = scan1.grab({'top': 917, 'left': 790, 'width': 1, 'height': 1})
			above_img = Image.frombytes('RGB', (above_scan.size.width, above_scan.size.height), above_scan.rgb)
   
   
			key_scan = scan1.grab({'top': 1097, 'left': 790, 'width': 1, 'height': 1})
			key_img = Image.frombytes('RGB', (key_scan.size.width, key_scan.size.height), key_scan.rgb)
			
			key_point = key_img.getpixel((0, 0))
			above_point = above_img.getpixel((0, 0))
			if key_point[0] > 230 and not toggle:
				keyboard.press('a')
				toggle = True
			elif toggle:
				if key_point[0] < 25 or key_point[0] < 70:
					keyboard.release('a')
					toggle = False
				elif above_point[0] < 150:
					time.sleep(0.06)
					keyboard.release('a')
					toggle = False

	elif current == 2:
		scan2 = mss()
		time.sleep(current/4)
		print("Second point activated")
		while True:
			above_scan = scan2.grab({'top': 917, 'left': 905, 'width': 1, 'height': 1})
			above_img = Image.frombytes('RGB', (above_scan.size.width, above_scan.size.height), above_scan.rgb)
   
   
			key_scan = scan2.grab({'top': 1097, 'left': 905, 'width': 1, 'height': 1})
			key_img = Image.frombytes('RGB', (key_scan.size.width, key_scan.size.height), key_scan.rgb)
			
			key_point = key_img.getpixel((0, 0))
			above_point = above_img.getpixel((0, 0))
			if key_point[1] > 200 and not toggle:
				keyboard.press('s')
				toggle = True
			elif toggle:
				if key_point[0] < 25 or key_point[1] < 62:
					keyboard.release('s')
					toggle = False
				elif above_point[1] < 140:
					time.sleep(0.06)
					keyboard.release('s')
					toggle = False
	elif current == 3:
		scan3 = mss()
		time.sleep(current/4)
		print("Third point activated")
		while True:
			above_scan = scan3.grab({'top': 917, 'left': 1015, 'width': 1, 'height': 1})
			above_img = Image.frombytes('RGB', (above_scan.size.width, above_scan.size.height), above_scan.rgb)
      
			key_scan = scan3.grab({'top': 1097, 'left': 1015, 'width': 1, 'height': 1})
			key_img = Image.frombytes('RGB', (key_scan.size.width, key_scan.size.height), key_scan.rgb)
			
			key_point = key_img.getpixel((0, 0))
			above_point = above_img.getpixel((0, 0))
			if key_point[1] > 200 and not toggle:
				keyboard.press('k')
				toggle = True
			elif toggle:
				if key_point[0] < 25 or key_point[1] < 62: 
					keyboard.release('k')
					toggle = False
				elif above_point[1] < 140: 
					time.sleep(0.06)
					keyboard.release('k')
					toggle = False
	elif current == 4:
		scan4 = mss()
		time.sleep(current/4)
		print("Last point activated")
		while True:
			above_scan = scan4.grab({'top': 917, 'left': 1130, 'width': 1, 'height': 1})
			above_img = Image.frombytes('RGB', (above_scan.size.width, above_scan.size.height), above_scan.rgb)
			
   
   
			key_scan = scan4.grab({'top': 1097, 'left': 1130, 'width': 1, 'height': 1})
			key_img = Image.frombytes('RGB', (key_scan.size.width, key_scan.size.height), key_scan.rgb)
			
			key_point = key_img.getpixel((0, 0))
			above_point = above_img.getpixel((0, 0))
			if key_point[0] > 230 and not toggle:
				keyboard.press('l')
				toggle = True
			elif toggle:
				if key_point[0] < 25 or key_point[0] < 70:
					keyboard.release('l')
					toggle = False
				elif above_point[0] < 150: 
					time.sleep(0.06)
					keyboard.release('l')
					toggle = False

if __name__ == '__main__':
	with get_context("spawn").Pool(4) as p:
		p.map(watch, current)
