#!C:\Users\ELCOT\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n")
import cgi
import pymysql
import os,random
import socket
import requests
form=cgi.FieldStorage()
fileid=form.getvalue('fileid')
seccode=form.getvalue('seccode')
decoyuser=form.getvalue('decoyuser')
hostname=socket.gethostname()
ipaddress=socket.gethostbyname(hostname)
try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="root",database="file_hacking")
    if(dbcon):
        cursor=dbcon.cursor()
        existsqry1="select * from tbl_fileupload where fileid=%d "%(int(fileid))
        cursor.execute(existsqry1)
        result=cursor.fetchone()
        ofileid=result[0]
        ownerid=result[1]
        ownername=result[2]
        filename=result[3]
        remoteurl=random.choice(os.listdir("../Admin_home_page/DecoyFiles/"))
        remotefile='http://localhost/FogComputing/Admin_home_page/DecoyFiles/%s'%(remoteurl)
        if(not os.path.exists("UserDownloadedFile/%s/"%("DecoyDownload"))):
            os.mkdir("UserDownloadedFile/%s/"%("DecoyDownload"))
                   
        localfile='UserDownloadedFile/%s/%s'%("DecoyDownload",remoteurl)
        data=requests.get(remotefile)
        with open(localfile,'wb') as file:
            if(file.write(data.content)):
                import datetime
                x=datetime.datetime.now()
                year=str(x.strftime("%Y"))
                month=str(x.strftime("%m"))
                day=str(x.strftime("%d"))
                downloaddate=str(day+"-"+month+"-"+year)

                        
                insertquery="insert into tbl_decoy(fileid,filename,ownername,decoyuser,downloadedon,fromipaddress)values(%d,'%s','%s','%s','%s','%s')"%(int(ofileid),filename,ownername,decoyuser,downloaddate,ipaddress)
                res=cursor.execute(insertquery)
                if(res==1):
                    dbcon.commit()
                    print("<script>alert('Downloaded and Save in %s');location.href='decoy.py';</script>"%(localfile))
                else:
                    dbcon.rollback()
                    print("<script>alert('Error in Downloading');location.href='decoy.py';</script>")
                            
              
    else:
            print("<script>alert('Error in DB');location.href='decoy.py';</script>")
except Exception as e:
    print(e)
