import time
from datetime import datetime
#https://www.youtube.com/watch?v=iWi4Z-5JNZw
timelimit = 18
currenttime = 0
#sites_to_block = ['www.youtube.com','youtube.com','www.youtube.de','youtube.de']
sites_to_block = ['www.facebook.com','facebook.com']
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def block_sites():
    already_done = 0
    while currenttime < timelimit: # block sites
        currenttime = datetime.now()
        currenttime = str(currenttime)
        currenttime = currenttime[11:13]
        time.sleep(600)
        if already_done < 1:
            already_done = 1
            with open(hosts_path, 'r+') as hostfile:#read-write ist r+
                hosts_content= hostfile.read()#alles in einen string
                for site in sites_to_block:
                    site = str(site)
                    if site not in hosts_content:
                        hostfile.write(redirect + " " + site + '\n')
    # block sites
    with open(hosts_path, 'r+') as hostsfile:
        lines = hostsfile.readlines()#liste wird erstellt
        hostsfile.seek(0)
        for line in lines:
            if not any(site in line for site in sites_to_block):
                hostsfile.write(line)
            hostsfile.truncate()#cut all the rest
block_sites()







