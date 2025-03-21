#!C:\Users\ELCOT\AppData\Local\Programs\Python\Python312\python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql
form=cgi.FieldStorage()
uname=form.getvalue('sname')
usertype=form.getvalue('stype')
try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="root",database="file_hacking")
    if(dbcon):
        cursor=dbcon.cursor()
        query="delete from tbl_user_session where username='%s' and usertype='%s'"%(uname,usertype)
        if(cursor.execute(query)>0):
            dbcon.commit()
            print("<script>alert('Session Destroyed');location.href='../index.py';</script>")
        else:
            dbcon.rollback()
            print("<script>alert('Error inDestroying');</script>")
    else:
        print("<script>alert('DB Error');</script>")
except Exception as e:
    print(e)
