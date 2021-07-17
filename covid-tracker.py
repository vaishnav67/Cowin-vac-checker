import requests
import time
from pushbullet import Pushbullet
from datetime import datetime, timedelta
def check_site(date):
    print(date)
	dist_id="Enter district id here"
    x = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id='+dist_id+'&date='+date)
    response = x.json()
    sessions = response['sessions']
    if(sessions==[]):
        print("No sessions\n")
    else:
        for i in sessions:
            if(i['available_capacity']!=0):
                pb = Pushbullet("API Token Here")
                dev = pb.get_device("Device Name Here")
                tt = "Date: "+date+"\nName: "+i['name']+"\nPincode: "+str(i['pincode'])+"\nAva. Capacity: "+str(i['available_capacity'])+"\nAva. Dose 1: "+str(i['available_capacity_dose1'])+"\nAva. Dose 2: "+str(i['available_capacity_dose2'])
                push = dev.push_note("Covid Details",tt)
            else:
                print(i['name']+" is empty, check again in 1 min.")
while(1):
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    check_site(date)
    now = datetime.now() + timedelta(days=1)
    date = now.strftime("%d-%m-%Y")
    check_site(date)
    time.sleep(60)
