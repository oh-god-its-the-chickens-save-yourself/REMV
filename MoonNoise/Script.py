import os
import sys
from time import sleep
from colorama import Fore
import pygame
from pygame.locals import *

# Initialize Audio
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)

os.system("clear")

print("MoonNoise. :)")
print("""
	+------------------------+
	|Created by Shaunak Ghosh|
	|Date: 23/03/2023 19:10  |
	|Github: shaunakg3       |
	+------------------------+
	\n
	""")

# Variables and Inputs
orange = input("How many Deep Craters are there that are highlighted are orange? ($/mesh.jpg)\n>>> ")
red = input("\nHow many Deep Craters are there that are highlighted are red? ($/mesh.jpg)\n>>> ")
yellow = input("\nHow many Deep Craters are there that are highlighted are yellow? ($/mesh.jpg)\n>>> ")
darkBlue = input("\nHow many Deep Craters are there that are highlighted are dark blue? ($/mesh.jpg)\n>>> ")
lightBlue = input("\nHow many Deep Craters are there that are highlighted are light blue? ($/mesh.jpg)\n>>> ")
totalCraters = input("\nHow many craters are on the moon in total (just google it.)\n>>> ")
orangeX = 2
redX = 1
yellowX = 1
darkBlueX = 1
lightBlueX = 5
iterations = 1675

# If Statements
def askif(variable, name):
	if variable == "idk":
		print("its ok, i know how you feel. if you don't know, check the file $/mesh.jpg\n")
		sleep(2)
		sys.exit()
	elif variable == "1" or variable == "2" or variable == "3":
		print("processing " + name + "...")
	else:
		print("try again later. :/ \n")

askif(orange, "voice")
sleep(1)
askif(red, "melody")
sleep(1)
askif(yellow, "drums")
sleep(1)
askif(darkBlue, "bass_regulator")
sleep(1)
askif(lightBlue, "bass")
sleep(1)
int(orange)
int(red)
int(yellow)
int(darkBlue)
int(lightBlue)
int(totalCraters)

# Functions

def loadMusic(x):
	pygame.mixer.music.load(x)

def voice():
	for i in range(orangeX):
		pygame.mixer.music.play()

def melody():
	for i in range(redX):
		pygame.mixer.music.play()

def drums():
	for i in range(yellowX):
		pygame.mixer.music.play()

def bass_regulator():
	for i in range(darkBlueX):
		pygame.mixer.music.play()

def bass():
	for i in range(lightBlueX):
		pygame.mixer.music.play()

def processMusic():
	for i in range(iterations):
		loadMusic("Audio/Voice.mp3")
		voice()
		loadMusic("Audio/Melody.mp3")
		melody()
		loadMusic("Audio/Drums.mp3")
		drums()
		loadMusic("Audio/Bass.mp3")
		bass_regulator()
		loadMusic("Audio/Melody.mp3")
		melody()
		loadMusic("Audio/Voice.mp3")
		voice()
		loadMusic("Audio/Bass.mp3")
		bass()

def start():
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()
	processMusic()

start()
