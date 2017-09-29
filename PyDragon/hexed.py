#!/usr/bin/python

class bcolors:
    global R,G
    P = '\033[95m' #PURPLE
    BL  = '\033[34m' #BLUE
    G = '\033[92m' #GREEN
    Y = '\033[93m' #YELLOW
    E = '\033[0m' #END
    B = '\033[1m' #BOLD
    U = '\033[4m' #UNDERLINE
    R  = '\033[31m' #RED
    C  = '\033[36m' # CYAN

def encrypt():
    hound = raw_input(R +  bcolors.U + 'String to encode>' + bcolors.E)
    hound = hound.encode('hex','strict');
    print ""+G+"Encoded: " + hound
def decrypt():
    hound = raw_input(R +  bcolors.U + 'String to decode>' + bcolors.E)
    hound = hound.decode('hex','strict');
    print ""+G+"Decoded String: " + hound
