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
            fn=os.path.basename(fp.filename)
            filefolder="DecoyFiles/"
                
                   
            if(os.path.exists(filefolder+"/"+fn)):
                print("<script>alert('FileName is Available');location.href='uploaddecoyfile.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
            else:
                open(filefolder+"/"+fn,'wb').write(fp.file.read())
                file_name=fp.filename
                print("<script>alert('File Uploaded');location.href='adminhomepage.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
                
                       
            
    else:
        print("<script>alert('DB Connection Error');location.href='uploaddecoyfile.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
except Exception as e:
    print("<script>alert('%s');location.href='uploaddecoyfile.py?sname=%s&stype=%s';</script>"%(sessname,sesstype))
                
