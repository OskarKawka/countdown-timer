import pyautogui
import time
from playsound import playsound
import os

# pyautogui.position()
programIsWorking = True


os.system('clear')
setSecAmount = 60 * int(input('After how many minutes should I shout?'))

countWhile = setSecAmount + 1  
while countWhile >= 0:
   for sec in range(setSecAmount, 0, -1):
      print('Alarm has been setted for ', setSecAmount//60, ' minutes and', setSecAmount%60, ' seconds.')
      print('Time left: ', sec//60, ' minutes ', sec%60, ' seconds')
      countWhile -= 1
      time.sleep(1)
      os.system('clear')
   break
print('Move your ass, bitch!')
playsound('/Users/oskarkawka/Documents/mixkit-rooster-crowing-in-the-morning-2462.wav')


    




