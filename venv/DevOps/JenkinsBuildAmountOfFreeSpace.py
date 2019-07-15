import os
myDiscstats = os.statvfs("/")
freeDisk = (myDiscstats.f_bfree * myDiscstats.f_frsize) / 1024**3
print ('There is a ', int(freeDisk), 'GB of available on your computer ')