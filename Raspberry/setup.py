import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def log(message, bcolor = ""):
    print(bcolor + message + bcolors.ENDC)


log("Starting Setup on your Raspberry pi...", bcolors.HEADER)

log("Please Enter Raspberry ID:", bcolors.BOLD)
while True:    
    raspberry_id = input()
    try:
        raspberry_id = int(raspberry_id)
    except ValueError:
        log("Error: The Raspberry ID is a integer number. try again...", bcolors.FAIL)
    else:
        log("OK.", bcolors.OKGREEN)
        break

log("Please Enter station coordinate:", bcolors.BOLD)
log("   for example : 33.776075, 55.085980")
log("                 <latitude, longitude>")
while True:    
    latlon = input()
    try:
        lat, lon = map(float, latlon.split(','))
    except ValueError:
        log("Error: Does not match the example provided. try again...", bcolors.FAIL)
    else:
        if lat < -90 or lat > 90 or lon < -180 or lon > 180:
            log("Error: Latitude or longitude are not allowed in the range. try again...", bcolors.FAIL)
            continue

        log("OK.", bcolors.OKGREEN)
        break

log("(1/5)  Set init Raspberry config...", bcolors.OKCYAN)
f = open("geolab.conf", 'a')
f.write(str(raspberry_id) + "\n")
f.write(str(lat) + "\n")
f.write(str(lon) + "\n")
f.close()

log("(2/5)  Install requirements packages...", bcolors.OKCYAN)
# os.system("pip install psycopg2-binary pandas numpy")

log("(3/5)  Install postgresql...", bcolors.OKCYAN)
# os.system("sudo apt install postgresql libpq-dev postgresql-client postgresql-client-common -y")

log("(4/5)  Create database...", bcolors.OKCYAN)
# 

log("(5/5)  Settings for automatic execution of the program...", bcolors.OKCYAN)
# 

log("OK.", bcolors.OKGREEN)
log("Will the system restart?(y/n)", bcolors.BOLD)
restart = input()

log("Good luck :)")

if restart == 'y':
    log("pass")
    # os.system("reboot")
