#Stefanos Michael
#227689

from calendar import *    #Libraries
from zipfile import *
from zlib import *
import os

fz=ZipFile("21century.zip","w",ZIP_DEFLATED)   #Zip File
for i in range(2000,2101):
    name=str(i)
    f=open(name+".txt","w")     #Open txt file for write
    year=int(name)
    a=calendar(year)    #Import calendar of each year
    f.write(a)     
    f.close()
    fz.write(name+".txt")         #Zip each txt file
    os.system("del "+name+".txt")      #Delete txt files
fz.close()

