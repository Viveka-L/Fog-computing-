#!C:\Users\ELCOT\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n")
import cgi
import pymysql
import os
try:
    import mscvcrt # Microsoft Visual C/C++ runtime lib
    msvcrt.setmode(0,os.O_BINARY) # stdin= 0
    msvcrt.setmode(1,os.O_BINARY) # stdout=1
except ImportError:
    pass

form=cgi.FieldStorage()
sessname=form.getvalue('oname')
sesstype=form.getvalue('otype')
print(sessname,sesstype)

try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="root",database="file_hacking")
    if(dbcon):
        cursor=dbcon.cursor()
        existsquery="select * from tbl_user_session where username='%s' and usertype='%s'"%(sessname,sesstype)
        if(cursor.execute(existsquery)==0):
            print("<script>alert('Session is Not Available');location.href='../index.py';</script>")
        else:
            fp=form['fileid']
            percheck="select * from tbl_register where username='%s' and usertype='%s' and status='%s'"%(sessname,sesstype,'Accept')
            if(cursor.execute(percheck)>0):
                fn=os.path.basename(fp.filename)
                filefolder="OwnerFiles/%s"%(sessname)
                if(not os.path.exists(filefolder)):
                   os.mkdir(filefolder)
                   
                if(os.path.exists(filefolder+"/"+fn)):
                    print("<script>alert('FileName is Available');location.href='ownerfileupload.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
                else:
                    open(filefolder+"/"+fn,'wb').write(fp.file.read())
                    file_name=fp.filename
                    #####
                    userqry="select userid,username from tbl_register where username='%s'"%(sessname)
                    cursor.execute(userqry)
                    result=cursor.fetchone()
                    userid=result[0]
                    username=result[1]
                    ###
                    autoqry="select ifnull(max(fileid),0) from tbl_fileupload"
                    cursor.execute(autoqry)
                    result1=cursor.fetchone()
                    fileid=result1[0]+1

                    ###
                    import datetime
                    x=datetime.datetime.now()
                    year=str(x.strftime("%Y"))
                    month=str(x.strftime("%m"))
                    day=str(x.strftime("%d"))
                    
                    uploaddate=str(day+"-"+month+"-"+year)
                    insertquery="insert into tbl_fileupload values(%d,'%s','%s','%s','%s')"%(int(fileid),userid,username,file_name,uploaddate)
                    result2=cursor.execute(insertquery)
                    if(result2==1):
                        dbcon.commit()
                        print("<script>alert('File Uploaded');location.href='ownerfileview.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
                    else:
                        dbcon.rollback()
                        print("<script>alert('Error in uploading Files');location.href='ownerfileupload.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
            else:
                print("<script>alert('You are Not Allowed to upload the files');location.href='ownerfileupload.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
    else:
        print("<script>alert('DB Connection Error');location.href='ownerfileupload.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
except Exception as e:
    print("<script>alert('%s');location.href='ownerfileupload.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
                
                    
                    
            
