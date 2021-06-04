from datetime import datetime
now = datetime.now()

if(now.hour >= 4 and now.hour <= 12):
    print("Buenos Dias, son las", now.hour)
elif(now.hour >= 13 and now.hour <= 18):
    print("Buenos Tardes, son las", now.hour)
else:
    print("Buenos Noches, son las", now.hour)
