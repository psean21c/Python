# https://pymotw.com/2/datetime/
import datetime, time

def runJob():
	print("good")
	ts = datetime.datetime.now()
	timestamp = str(ts.hour) + "-" + str(ts.minute)
	print(str(ts) + ":\t" + timestamp)
	
	today = datetime.date.today()
	print(today)
	
	suffix = str(today) + "-" + timestamp
	print(suffix)

if __name__ == "__main__":
	runJob()
	
