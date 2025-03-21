#!C:\Users\ELCOT\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n")
import cgi
import pymysql
form=cgi.FieldStorage()
oid=form.getvalue('oid')
oname=form.getvalue('oname')
opwd=form.getvalue('opwd')
ofname=form.getvalue('ofname')
olname=form.getvalue('olname')
oaddress=form.getvalue('oaddress')
ocity=form.getvalue('ocity')
ostate=form.getvalue('ostate')
ocountry=form.getvalue('ocountry')
omobile=form.getvalue('omobile')
oemail=form.getvalue('oemail')
print(ofname)
print(olname)
print(opwd)

try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="root",database="file_hacking")
    if(dbcon):
        cursor=dbcon.cursor()
        updatequery="update tbl_register set firstname='%s',lastname='%s',address='%s',city='%s',state='%s',country='%s' where userid=%d and username='%s' and password='%s' and mobile_number='%s' and email_id='%s' "%(ofname,olname,oaddress,ocity,ostate,ocountry,int(oid),oname,opwd,omobile,oemail)
        print(updatequery)
        res=cursor.execute(updatequery)
        if(res==1):
            dbcon.commit()
            print("<script>alert('Updated success');location.href='ownerhomepage.py?sname=%s&stype=%s';</script>"%(oname,'Owner'))
        else:
            dbcon.rollback()
            #print("<script>alert('Error in Updation');location.href='ownerhomepage.py?sname=%s&stype=%s';</script>"%(oname,'Owner'))
    else:
        print("<script>alert('DB Error');location.href='ownerhomepage.py?sname=%s&stype=%s';</script>"%(oname,'Owner'))
except Exception as e:
    print(e)
              
    
            
                                                                                                                                                                                                                                                                             
