import os
from dotenv import load_dotenv
load_dotenv()

import socket
import threading
import time

import keyboard

import pyautogui
pyautogui.PAUSE = 0.1

# import env settings
SERVER = os.getenv("SERVER")
PORT = os.getenv("PORT")
PASS = os.getenv("PASS")
BOT = os.getenv("BOT")
CHANNEL = os.getenv("CHANNEL")
OWNER = os.getenv("OWNER")

message = ""

#actiondelay = 1
#movedelay = 0	


irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send((  "PASS " + PASS + "\n" +
			"NICK " + BOT + "\n" +
			"JOIN #" + CHANNEL + "\n").encode())
				
					
def gamecontrol():

	global message
	step = 1
	move = ""

	while True:
		
		try: #try to prevent error when different key is pressed
			if keyboard.is_pressed('p') and keyboard.is_pressed('o'): # and timer = 0: #if key 'q' is pressed 
				print('Pausing 20 sec')
				time.sleep(20)	
			else:				
				pass
		except:
			pass
		
		message = message.lower()
		
		
		if message != "":
			if step == 1:
				movetemp = message
				print(movetemp)
				try:
					move = movetemp.split(',', 1)[0]
					print(move)
				except:
					continue
			
			if step == 2:
				try:
					move = movetemp.split(',', 1)[1]
					print(move)
				except:
					step = 1
					move = ""
					movetemp = ""
					message = ""		
		else:
			pass
		
		
#Execute movement

		if "face" in move: 
			pyautogui.moveTo(960, 825, duration=1)
			pyautogui.click()
		elif "end" in move: 
			pyautogui.moveTo(1560, 490, duration=1)
			pyautogui.click()
		elif "smorc" in move: 
			pyautogui.moveTo(960, 200, duration=1)
			pyautogui.click()
		elif "hp" in move: 
			pyautogui.moveTo(1130, 825, duration=1)
			pyautogui.click()

#Player minions			

		elif "b10" in move: 
			pyautogui.moveTo(1165, 595, duration=1)
			pyautogui.click()
		elif "b11" in move: 
			pyautogui.moveTo(1230, 595, duration=1)
			pyautogui.click()
		elif "b12" in move: 
			pyautogui.moveTo(1300, 595, duration=1)
			pyautogui.click()
		elif "b13" in move: 
			pyautogui.moveTo(1370, 595, duration=1)
			pyautogui.click()
		elif "b1" in move: 
			pyautogui.moveTo(540, 595, duration=1)
			pyautogui.click()
		elif "b2" in move: 
			pyautogui.moveTo(610, 595, duration=1)
			pyautogui.click()
		elif "b3" in move: 
			pyautogui.moveTo(680, 595, duration=1)
			pyautogui.click()
		elif "b4" in move: 
			pyautogui.moveTo(750, 595, duration=1)
			pyautogui.click()
		elif "b5" in move: 
			pyautogui.moveTo(820, 595, duration=1)
			pyautogui.click()
		elif "b6" in move: 
			pyautogui.moveTo(890, 595, duration=1)
			pyautogui.click()
		elif "b7" in move: 
			pyautogui.moveTo(960, 595, duration=1)
			pyautogui.click()
		elif "b8" in move: 
			pyautogui.moveTo(1030, 595, duration=1)
			pyautogui.click()
		elif "b9" in move: 
			pyautogui.moveTo(1090, 595, duration=1)
			pyautogui.click()
			
#Enemy minions
		
		elif "e10" in move: 
			pyautogui.moveTo(1165, 400, duration=1)
			pyautogui.click()
		elif "e11" in move: 
			pyautogui.moveTo(1230, 400, duration=1)
			pyautogui.click()
		elif "e12" in move: 
			pyautogui.moveTo(1300, 400, duration=1)
			pyautogui.click()
		elif "b13" in move: 
			pyautogui.moveTo(1370, 400, duration=1)
			pyautogui.click()
		elif "e1" in move: 
			pyautogui.moveTo(540, 400, duration=1)
			pyautogui.click()
		elif "e2" in move: 
			pyautogui.moveTo(610, 400, duration=1)
			pyautogui.click()
		elif "e3" in move: 
			pyautogui.moveTo(680, 400, duration=1)
			pyautogui.click()
		elif "e4" in message: 
			pyautogui.moveTo(750, 400, duration=1)
			pyautogui.click()
		elif "e5" in move: 
			pyautogui.moveTo(820, 400, duration=1)
			pyautogui.click()
		elif "e6" in move: 
			pyautogui.moveTo(890, 400, duration=1)
			pyautogui.click()
		elif "e7" in move: 
			pyautogui.moveTo(960, 400, duration=1)
			pyautogui.click()
		elif "e8" in move: 
			pyautogui.moveTo(1030, 400, duration=1)
			pyautogui.click()
		elif "e9" in move: 
			pyautogui.moveTo(1090, 400, duration=1)
			pyautogui.click()
			
#Hand
		
		elif "h10" in move: 
			pyautogui.moveTo(1160, 1055, duration=1)
			pyautogui.click()
		elif "h1" in move: 
			pyautogui.moveTo(645, 1060, duration=1)
			pyautogui.click()
		elif "h2" in move: 
			pyautogui.moveTo(700, 1040, duration=1)
			pyautogui.click()
		elif "h3" in move: 
			pyautogui.moveTo(755, 1025, duration=1)
			pyautogui.click()
		elif "h4" in move: 
			pyautogui.moveTo(810, 1020, duration=1)
			pyautogui.click()
		elif "h5" in move: 
			pyautogui.moveTo(865, 1010, duration=1)
			pyautogui.click()
		elif "h6" in move: 
			pyautogui.moveTo(930, 990, duration=1)
			pyautogui.click()
		elif "h7" in move: 
			pyautogui.moveTo(980, 1000, duration=1)
			pyautogui.click()
		elif "h8" in move: 
			pyautogui.moveTo(1030, 1010, duration=1)
			pyautogui.click()
		elif "h9" in move: 
			pyautogui.moveTo(1080, 1035, duration=1)
			pyautogui.click()
		else:
			continue
			
		if step >= 2:
			step = 1
			message = ""
			move = ""
			time.sleep(2)
		else:
			step = step + 1




def twitch():
	def joinchat():
		Loading = True
		while Loading:
			readbuffer_join = irc.recv(1024)
			readbuffer_join = readbuffer_join.decode()
			for line in readbuffer_join.split("\n")[0:-1]:
				print(line)
				Loading = loadingComplete(line)

	def loadingComplete(line):
		if("End of /NAMES list" in line):
			print("Bot has joinded " + CHANNEL)
			sendMessage(irc, "Chat Room Joined")
			return False
		else:
			return True
			
	def sendMessage(irc, message):
		messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
		irc.send((messageTemp + "\n").encode())
	def getUser(line):
		seperate = line.split(":", 2)
		user = seperate[1].split("!", 1)[0]
		return user
	def getMessage(line):
		global message
		
		try:
			message = (line.split(":", 2))[2]
		except:
			message = ""
		return message
	
	def Console(line):
		if "PRIVMSG" in line:
			return False
		else:
			return True
		
	joinchat()

	while True:
		try:
			readbuffer = irc.recv(1024).decode()
		except:
			readbuffer = ""
		for line in readbuffer.split("\r\n"):
			if line == "":
				continue
			elif "PING" in line and Console(line):
				msgg = "PONG tmi.twitch.tv\r\n".encode()
				irc.send(msgg)
				print(msgg)
				continue
			else:
				user = getUser(line)
				message = getMessage(line)
				message = message.lower()
				
				print(user + " : " + message)
		

if __name__ == '__main__':
	t1 = threading.Thread(target = twitch)
	t1.start()
	t2 = threading.Thread(target = gamecontrol)
	t2.start()
	