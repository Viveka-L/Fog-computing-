#!C:\Users\ELCOT\AppData\Local\Programs\Python\Python312/python.exe
print("content-type:text/html\r\n")
import cgi
import pymysql
form=cgi.FieldStorage()
sessname=form.getvalue('sname')
sesstype=form.getvalue('stype')
try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="root",database="file_hacking")
    if(dbcon):
        cursor=dbcon.cursor()
        existsquery="select * from tbl_user_session where username='%s' and usertype='%s'"%(sessname,sesstype)
        if(cursor.execute(existsquery)==0):
            print("<script>alert('Session is Not Available');location.href='../index.py';</script>")
        else:
                print("""

                <!DOCTYPE html>
                <html lang="en">

                <head>

                    <meta charset="utf-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <meta name="description" content="">
                    <meta name="author" content="">

                    <title>File Hacking</title>

                    <!-- Bootstrap Core CSS -->
                    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

                    <!-- Custom Fonts -->
                    <link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
                    <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>
                    <link href='https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic,900,900italic' rel='stylesheet' type='text/css'>

                    <!-- Plugin CSS -->
                    <link href="vendor/magnific-popup/magnific-popup.css" rel="stylesheet">

                    <!-- Theme CSS -->
                    <link href="css/creative.min.css" rel="stylesheet">

                    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
                    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
                    <!--[if lt IE 9]>
                        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
                        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
                    <![endif]-->

                </head>

                <body id="page-top">

                    <nav id="mainNav" class="navbar navbar-default navbar-fixed-top">
                        <div class="container-fluid">
                            <!-- Brand and toggle get grouped for better mobile display -->
                            <div class="navbar-header">
                                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                                    <span class="sr-only">Toggle navigation</span> Menu <i class="fa fa-bars"></i>
                                </button>
                                <a class="navbar-brand page-scroll" href="#page-top">Fog Computing</a>
                            </div>

                            <!-- Collect the nav links, forms, and other content for toggling -->
                            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                                <ul class="nav navbar-nav navbar-right">""")
                print("<li><a class='page-scroll' href='ownermyprofile.py?sname=%s&stype=%s'>My Profile</a></li>"%(sessname,sesstype))
                print("<li><a class='page-scroll' href='ownerfileupload.py?sname=%s&stype=%s'>File Upload</a></li>"%(sessname,sesstype))
                print("<li><a class='page-scroll' href='ownerfileview.py?sname=%s&stype=%s'>File View</a></li>"%(sessname,sesstype))
                print("<li><a class='page-scroll' href='ownerviewuser.py?sname=%s&stype=%s'>User Download</a></li>"%(sessname,sesstype))
                print("<li><a class='page-scroll' href='logout.py?sname=%s&stype=%s'>Logout</a></li>"%(sessname,sesstype))
                      
                print("""</ul>
                            </div>
                            <!-- /.navbar-collapse -->
                        </div>
                        <!-- /.container-fluid -->
                    </nav>

                    <header>
                        <div class="header-content">
                            <div class="header-content-inner">
            <div class="modal-body">
                <form  action="ownerfileupload_action.py"class="form-horizontal" method='post' enctype='multipart/form-data'>
                 <div class="control-group">
                      
                    <table width=50% align=center border=0>
                      <tr><td align=left>File Upload</td></tr>""")
                print("<tr><td><input type='hidden' name='oname' value='%s'></td><td><input type='hidden' name='otype' value='%s'></td></tr>"%(sessname,sesstype))
                print("<tr><td><input type='file'  name='fileid' id='inputname' required></td>")
                print("<td><input type='submit' style='width:200px;height:50px;background-color:silver;' name='osubmit' id='inputname' value='Upload'></td></tr>")
                print("""</table>            
                            
                            </div>
                        </div>
                    </header>

                    
                    <!-- jQuery -->
                    <script src="vendor/jquery/jquery.min.js"></script>

                    <!-- Bootstrap Core JavaScript -->
                    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>

                    <!-- Plugin JavaScript -->
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
                    <script src="vendor/scrollreveal/scrollreveal.min.js"></script>
                    <script src="vendor/magnific-popup/jquery.magnific-popup.min.js"></script>

                    <!-- Theme JavaScript -->
                    <script src="js/creative.min.js"></script>

                </body>

                </html>
                """)
    else:
        print("<script>alert('DB Error');location='index.py';</script>")
except Exception as e:
    print(e)
