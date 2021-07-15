import requests
import time
from pushbullet import Pushbullet
from datetime import datetime
while(1):
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
	district_id="1"
    x = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id='+district_id+'&date='+date)
    response = x.json()
    sessions = response['sessions']
    if(sessions==[]):
        print("No sessions\n")
    else:
        pb = Pushbullet("API Token Here")
        dev = pb.get_device('Device Name Here')
        for i in sessions:
            if(i['available_capacity']!=0 or i['available_capacity_dose1']!=0):
                tt = "Name: "+i['name']+"\nPincode: "+str(i['pincode'])+"\nAva. Capacity: "+str(i['available_capacity'])+"\nAva. Dose 1: "+str(i['available_capacity_dose1'])+"\nAva. Dose 2: "+str(i['available_capacity_dose2'])
                push = dev.push_note("Covid Details",tt)
            else:
                print(i['name']+" is empty, check again in 5 mins.")
    time.sleep(300)