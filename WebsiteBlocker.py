""" 
----------------------------------------
Website Blocker
----------------------------------------
We all know while surfing through the net many unwanted sites 
popup to distract us. This project comes at help in such cases 
as it can be built up to block certain websites from opening. 
The program is beneficial for people who get easily distracted 
to switch to social media sites while into something serious.
----------------------------------------
"""

import time
from datetime import datetime as dt


hosts_path = r"/etc/hosts"   # r is for raw string
hosts_temp = "hosts"
redirect = "127.0.0.1"
web_sites_list = ["www.facebook.com", "facebook.com"]    # users can modify the list of the websites they want to block

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,22):
        print("Working hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in web_sites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun time")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)  # reset the pointer to the top of the text file
            for line in content:
            # here comes the tricky line, basically we overwrite the whole file
                if not any(website in line for website in web_sites_list):
                    file.write(line)
                # do nothing otherwise
            file.truncate() # this line is used to delete the trailing lines (that contain DNS)
    time.sleep(5)