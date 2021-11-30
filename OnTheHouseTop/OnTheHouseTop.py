import playsound
import schedule
import time

def song():
	print("song")
	playsound.playsound("OnTheHouseTop.mp3")
	
schedule.every().day.at("09:00").do(song)

while 1:
	schedule.run_pending()
	time.sleep(1)