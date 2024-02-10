import time
import sys
import os
libdir = "./lib/"
import logging
from RPi_FLH import RPi_FLH
 
logging.basicConfig(level=logging.INFO)

POE = RPi_FLH.RPi_FLH()
        
try:  
    while(1):
        POE.POE_HAT_Display(43)
        time.sleep(1)
        
except KeyboardInterrupt:    
    print("ctrl + c:")
    POE.FAN_OFF()