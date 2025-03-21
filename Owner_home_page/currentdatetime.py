import datetime

x=datetime.datetime.now()
year=str(x.strftime("%Y"))
month=str(x.strftime("%M"))
day=str(x.strftime("%d"))

uploaddate=str(day+"-"+month+"-"+year)
print(uploaddate)

logtime=x.strftime("%H:%M:%S")
print(logtime)

