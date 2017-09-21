import numpy as np
import re
import sys
import time
import os.path
from string import Template
import struct
import logging
import threading
import zipfile
class mylog(logging.Logger):
    def __init__(self):
        logging.Logger.__init__(self,'mylog')
mylog().info('ss')        

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)
    

background = AsyncZip('test.txt', 'test.zip')
background.start()
print('The main program continues to run in foreground.')
#print(background._target)
background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
