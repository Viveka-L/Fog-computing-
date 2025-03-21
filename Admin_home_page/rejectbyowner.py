#!C:\Users\ELCOT\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n")
import cgi
import pymysql
form=cgi.FieldStorage()
oid=form.getvalue('q')
oemail=form.getvalue('sid')

try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="root",database="file_hacking")
    if(dbcon):
        cursor=dbcon.cursor()
        updatequery="update tbl_register set status='%s' where userid=%d  and email_id='%s' "%('Reject',int(oid),oemail)
        res=cursor.execute(updatequery)
        if(res==1):
            dbcon.commit()
            print("<script>alert('Updated success');location.href='manageowners.py?sname=%s&stype=%s';</script>"%('Admin','Admin'))
        else:
            dbcon.rollback()
            print("<script>alert('Error in Updation');location.href='manageowners.py?sname=%s&stype=%s';</script>"%('Admin','Admin'))
    else:
        print("<script>alert('Error in Updation');location.href='manageowners.py?sname=%s&stype=%s';</script>"%('Admin','Admin'))
except Exception as e:
    print(e)
              
    
            
                                                                                                                                                                                                                                                                             
