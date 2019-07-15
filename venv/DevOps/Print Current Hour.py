# Create New Text File
import time
myTime = open("/users/adiellevy/Desktop/time.txt",'w',encoding='utf-8')
myHour = time.asctime(time.localtime(time.time()))


#myTime.write('adiel')
#myTime.close()
