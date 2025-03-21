#!C:\Users\ELCOT\AppData\Local\Programs\Python\Python312\python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql
import math,random
import smtplib,ssl
form=cgi.FieldStorage()
uname=form.getvalue('uname')
email=form.getvalue('email')
mobilenumber=form.getvalue('mobilenumber')
password=form.getvalue('password')
usertype=form.getvalue('usertype')
try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="root",database="file_hacking")
    if(dbcon):
        cursor=dbcon.cursor()
        existsquery="select * from tbl_register where username='%s' and password='%s' and mobile_number='%s' and email_id='%s' and usertype='%s'"%(uname,password,mobilenumber,email,usertype)
        if(cursor.execute(existsquery)>0):
            print("<script> alert('Already Exist');location.href='index.py';</script>")
        else:
            squery="select ifnull(max(userid),0) from tbl_register"
            cursor.execute(squery)
            result=cursor.fetchone()
            usrid=result[0]+1
            otp=''
            string='01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            length=len(string)
            for i in range(6):
                otp+=string[int(random.random()*length)]
            insertquery="insert into tbl_register(userid,username,password,security_code,mobile_number,email_id,usertype,status)values(%d,'%s','%s','%s','%s','%s','%s','%s')"%(int(usrid),uname,password,otp,mobilenumber,email,usertype,'Status')
            res=cursor.execute(insertquery)
            if(res==1):
                dbcon.commit()
                
                    
                smtp_server='smtp.gmail.com'
                port=587
                sender_email=''
                password=""
                context=ssl.create_default_context()
                try:
                    server=smtplib.SMTP(smtp_server,port)
                    server.ehlo()
                    server.starttls(context=context)
                    server.ehlo()
                    server.login(sender_email,password)
                    receiver_email=email
                    message=otp
                    server.sendmail(sender_email,receiver_email,message)
                    print("<script>alert('signup success!Code Sent to MailId');location.href='index.py';</script>")
                    
                except Exception as e:
                    print("<script>alert('Error in Sending Mail');location.href='index.py';</script>")
                    print(e)
                finally:
                    server.quit()
                
            else:
                dbcon.rollback()
                print("<script>alert('Error in register');location.href='signup.py';</script>")
    else:
        print("<script>alert('Error in register');location='index.py';</script>")
except Exception as e:
    print(e)
              
    
            
                                                                                                                                                                                                                                                                             
