#!C:\Users\ELCOT\AppData\Local\Programs\Python\Python312\python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql
import socket
form=cgi.FieldStorage()
uname=form.getvalue('uname')
password=form.getvalue('password')
usertype=form.getvalue('usertype')

try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="root",database="file_hacking")
    if(dbcon):
        cursor=dbcon.cursor()
        if(usertype=="Owner"):
            
            existsquery="select * from tbl_register where username='%s' and  password='%s' and usertype='%s'"%(uname,password,usertype)
            if(cursor.execute(existsquery)>0):
                insertquery="insert into tbl_user_session values('%s','%s','%s')"%(uname,password,usertype)
                res=cursor.execute(insertquery)
                if(res==1):
                    dbcon.commit()
                    print("<script>alert('SignIn success');location.href='Owner_home_page/ownerhomepage.py?sname=%s&stype=%s';</script>"%(uname,usertype))
                else:
                    dbcon.rollback()
                    print("<script>alert('Error in Login');location.href='index.py';</script>")
            else:
                print("<script>alert('Invalid User Name or Password');location.href='index.py';</script>")
        elif(usertype=="User"):
            hostname=socket.gethostname()
            ipaddr=socket.gethostbyname(hostname)
            existsquery="select userid from tbl_register where username='%s' and  password='%s' and usertype='%s'"%(uname,password,usertype)
            if(cursor.execute(existsquery)>0):
                getuserid=cursor.fetchone()
                loggeduser=getuserid[0]
                insertquery="insert into tbl_user_session values('%s','%s','%s')"%(uname,password,usertype)
                res=cursor.execute(insertquery)
                if(res==1):
                    dbcon.commit()
                    logdel="delete from loginlogs where ipaddress='%s'"%(ipaddr)
                    cursor.execute(logdel)
                    print("<script>alert('SignIn success');location.href='User_home_page/userhomepage.py?sname=%s&stype=%s';</script>"%(uname,usertype))
                else:
                    dbcon.rollback()
                    print("<script>alert('Error in Login');location.href='index.py';</script>")
            else:
                import datetime
                x=datetime.datetime.now()
                logtime=x.strftime("%H:%M:%S")
                print(logtime)
                hostname=socket.gethostname()
                ipaddr=socket.gethostbyname(hostname)
                
                logqry="select count(*) as total_count from loginlogs where  ipaddress='%s'"%(ipaddr)
                cursor.execute(logqry)
                logresult=cursor.fetchone()
                totalcount=logresult[0]
                if(totalcount>3):
                    print("<script>alert('logged in');location.href='User_home_page/decoy.py?q=%s';</script>"%(uname))
                else:
                    totalcount=totalcount
                    remattempt=4-totalcount
                    if(remattempt==0):
                        print("<script>alert('Too Many Login Attempts.Please login after 30 seconds');location.href='index.py';</script>")
                    else:
                        sql="select ifnull(max(logid),0) from loginlogs"
                        cursor.execute(sql)
                        res1=cursor.fetchone()
                        logidcount=res1[0]+1
                        insertlog="insert into loginlogs values(%d,'%s','%s')"%(int(logidcount),ipaddr,logtime)
                        print(insertlog)
                        cursor.execute(insertlog)
                        dbcon.commit()
                        print("<script>alert('Please Enter Valid Login Details %s attempts remaining');location.href='index.py';</script>"%(remattempt))

                
        elif(usertype=="Admin"):
            if(uname=='Admin' and password=="Admin"):
                insertquery="insert into tbl_user_session values('%s','%s','%s')"%(uname,password,usertype)
                res=cursor.execute(insertquery)
                if(res==1):
                    dbcon.commit()
                    print("<script>alert('SignIn success');location.href='Admin_home_page/adminhomepage.py?sname=%s&stype=%s';</script>"%(uname,usertype))
                else:
                    dbcon.rollback()
                    print("<script>alert('Error in Login');location.href='index.py';</script>")
            else:
                
                print("<script>alert('Invalid User Name or Password');location.href='index.py';</script>")
        
        else:
            print("<script>alert('Invalid UserType');location.href='index.py';</script>")
    else:
        print("<script>alert('Error in register');location='index.py';</script>")
except Exception as e:
    print(e)
              
    
            
                                                                                                                                                                                                                                                                             
