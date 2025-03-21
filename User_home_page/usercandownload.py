#!C:\Users\ELCOT\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n")
import cgi
import pymysql
import requests
import os
form=cgi.FieldStorage()
sessname=form.getvalue('sname')
sesstype=form.getvalue('stype')
fileid=form.getvalue('fileid')
userid=form.getvalue('userid')
seccode=form.getvalue('seccode')

try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="root",database="file_hacking")
    if(dbcon):
        cursor=dbcon.cursor()
        existsquery="select * from tbl_user_session where username='%s' and usertype='%s'"%(sessname,sesstype)
        if(cursor.execute(existsquery)==0):
            print("<script>alert('Session is Not Available');location.href='../index.py';</script>")
        else:
            existsqry="select * from tbl_register where username='%s' and security_code='%s' and usertype='%s'"%(sessname,seccode,sesstype)
            if(cursor.execute(existsqry)>0):
                getdata=cursor.fetchone()
                sessid=getdata[0]
                existsqry1="select * from tbl_fileupload where fileid=%d and userid=%d"%(int(fileid),int(userid))
                cursor.execute(existsqry1)
                result=cursor.fetchone()
                ofileid=result[0]
                ownerid=result[1]
                ownername=result[2]
                filename=result[3]
                remoteurl='http://localhost/FogComputing/Owner_home_page/OwnerFiles/%s/%s'%(ownername,filename)
                if(not os.path.exists("UserDownloadedFile/%s/"%(sessname))):
                   os.mkdir("UserDownloadedFile/%s/"%(sessname))
                   
                localfile='UserDownloadedFile/%s/%s'%(sessname,filename)
                data=requests.get(remoteurl)
                with open(localfile,'wb') as file:
                    if(file.write(data.content)):
                        import datetime
                        x=datetime.datetime.now()
                        year=str(x.strftime("%Y"))
                        month=str(x.strftime("%m"))
                        day=str(x.strftime("%d"))
                        downloaddate=str(day+"-"+month+"-"+year)
                        insertquery="insert into tbl_download(fileid,ownerid,fileowner,userid,username,filename,downloadedon)values(%d,%d,'%s',%d,'%s','%s','%s')"%(int(ofileid),int(ownerid),ownername,int(sessid),sessname,filename,downloaddate)
                        res=cursor.execute(insertquery)
                        if(res==1):
                            dbcon.commit()
                            print("<script>alert('Downloaded and Save in %s');location.href='userfiledownload.py?sname=%s&stype=%s';</script>"%(localfile,sessname,sesstype))
                        else:
                            dbcon.rollback()
                            print("<script>alert('Error in Downloading');location.href='userfiledownload.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
                            
                    else:
                        print("<script>alert('Error in Downloading');location.href='userfiledownload.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
                    
            else:
                
                print("<script>alert('Wrong Security Code');location.href='userfiledownload.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
    else:
            print("<script>alert('Error in DB');location.href='userfiledownload.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
except Exception as e:
    print(e)
