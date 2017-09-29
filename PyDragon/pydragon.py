#PYDRAGON
#THIS AUTOMATION SCRIPT IS STILL IN DEVELOPMENT
#plz report bugs on my email or github
#CREDITS : 526f79616c2e4e696e6a61
#CONTACT : royalninja0702@gmail.com
#-->  <--

import os,sys
import time
import platform
import metasploit
import requests
from banner import *
from hexed import *

class bcolors:
    P = '\033[95m' #PURPLE
    BL  = '\033[34m' #BLUE
    G = '\033[92m' #GREEN
    Y = '\033[93m' #YELLOW
    E = '\033[0m' #END
    B = '\033[1m' #BOLD
    U = '\033[4m' #UNDERLINE
    R  = '\033[31m' #RED
    C  = '\033[36m' # CYAN
class agree():
    os.system('clear')
    ############# SYSTEM CHECKS STARTS #########
    if str(platform.system()) != "Linux":
        sys.exit("[!] " + bcolors.U + "\033[91m" + "You are not using a Linux Based OS! Linux is a must-have for this script!" + color.E)
    if not os.geteuid() == 0:
        sys.exit("[!] " + bcolors.U + "\033[91m" + "Must be run as root. :/" + color.E)
    ############# SYSTEM CHECKS ENDS #########
    ############# AGREEMENT STARTS #############
    if 'no' in open('agree.txt').read():#take out of pydragon/
        print bcolors.R + """
            Note that pydragon is an open-source application.

            Feel free to modify, use, change, market, do whatever you want with it as long as you give the appropriate credit where credit is due (which   means giving the authors the credit they deserve for writing it) changing name in credits won't make you a coder.
            """
        agree = raw_input(bcolors.U + 'Do you agree to these terms and conditions?>' + bcolors.E)
        if agree == "yes":
            print (bcolors.U + 'Thanks!' + bcolors.E)
            time.sleep(3)
            FILE = open("agree.txt","w")
            FILE.write('yes')
            FILE.close()
        elif agree == "y":
            print (bcolors.U + 'Thanks!' + bcolors.E)
            time.sleep(3)
    	    FILE = open("agree.txt","w")
            FILE.write('yes')
            FILE.close()
        elif agree == "Yes":
           print (bcolors.U + 'Thanks!' + bcolors.E)
           FILE = open("agree.txt","w")
           FILE.write('yes')
           FILE.close()
        else:
            print (bcolors.U + '[!] You have to agree!' + bcolors.E)
    	    time.sleep(3)
            sys.exit()
        ############# AGREEMENT ENDS #############
obj=agree()
class pydragon():
    os.system('clear')
    def __init__(self):
        print ""
        time.sleep(0.1)
        print bcolors.B + bcolors.G + "-----> Made by 526f79616c2e4e696e6a61 <-----"
        time.sleep(0.1)
        print bcolors.BL + "----->          Version: 1.0          <-----"
        time.sleep(0.1)
        print bcolors.Y + "----->       #1 tool for Pentesting   <-----"
        time.sleep(0.1)
        print bcolors.C + "\n----->     Welcome to PyDragon!       <-----"
        time.sleep(0.1)
        print bcolors.Y + "----->     Awesome Pentesting tool!   <-----" + bcolors.E
        time.sleep(0.3)
        try:
            r=requests.get('https://www.google.co.in/')
        except:
            print "" + R +  '\033[1m' + bcolors.U + "Please connect to internet to Run the script"
            time.sleep(2)
            sys.exit()
    def info(self):
        ############# SYSTEM INFO START #############
        uname = os.popen('uname -a').read()
        print bcolors.BL + "\n* User : " + os.popen('whoami').read().strip()
        time.sleep(0.2)
        print "* Group : " + os.popen('id -Gn').read().strip()[:20]
        time.sleep(0.2)
        print "* Kernel : " + os.popen('uname -r').read().strip() + bcolors.E + "\n"
        time.sleep(1)
        ############# SYSTEM INFO ENDS #############
    def options(self):
################################################
#~~~~~~~~~~NOTHING FOR NOOBS HERE~~~~~~~~~~~~~~#
################################################
        while True:
            try:
                try:
                    main=raw_input(bcolors.B + "PYDRAGON> " + bcolors.E)
                    if main == "h":
                        time.sleep(0.2)
                        os.system("gnome-terminal -e 'bash -c \"msfconsole; exec bash\"'")
                    elif main == "Encode":
                        encrypt()
                    elif main == "Decode":
                        decrypt()
                    elif main == "Exit":
                        print (R  + bcolors.U + "\033[1m" + "Exixting..." + bcolors.E)
                        print (bcolors.BL + bcolors.U + "\033[1m" + "GoodBye!" + bcolors.E)
                        time.sleep(0.9)
                        sys.exit()
                    elif main == "Print":
                        banner()
                    elif main == "Help":
                        print ""+ R +"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                        print ""+ C +"Help" '\033[1m' + U + "Displays the Help message! "
                        print ""+ C +"Print" '\033[1m' + U + "Prints a new banner "        ### !!! UNDER CONSTRUCTION !!! ###
                        print ""+ C +"Exit" '\033[1m' + U + "Closes the tool "
                        print ""+ C +"Encode" '\033[1m' + U + "Text to Hex "
                        print ""+ C +"Decode" '\033[1m' + U + "Hex to Text "
                    else:
                        print bcolors.R + "check your input" + bcolors.E
                        time.sleep(1)
                except KeyboardInterrupt:
                    print (R + bcolors.U  + "\033[1m" + "\nCtrl-C Pressed! Use 'Exit' to close the tool!" + bcolors.E)
                    pass
            except EOFError:
                print (R + bcolors.U  + "\033[1m" + "\nCtrl-D Pressed! Use 'Exit' to close the tool!" + bcolors.E)
                pass
obj=pydragon()
obj.info()
obj.options()
