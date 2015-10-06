# -*- coding: cp1253 -*-
from smtplib import *
pasxa=""
for ages in range(2001,2101):
    m19=19*(ages%19)
    z1=16+m19
    n2=z1%30
    m2=2*(ages%4)
    m4=4*(ages%7)
    z=6*n2+m4+m2
    n1=z%7
    p=n1+n2
    k=3+p
    if k<=30:
        month="Απριλίου"
    else:
        month="Μαίου"
        k=k-30
    pasxa+="Η ημερομηνία του Πάσχα για τη χρονιά "+ " "+str(ages)+ " "+"είναι "+ str(k)+" "+ str(month)+"."+"\n"
print pasxa


    
server=SMTP("patreas.upatras.gr")
message=pasxa
server.sendmail("ece7689@upnet.gr","ece7689@upnet.gr",message)
