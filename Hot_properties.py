def login():
    sr_no=0
    import pymysql as sq
    import warnings as wa
    wa.filterwarnings(action='ignore')
    con=sq.connect('localhost','root','1234','abc')
    cur=con.cursor()
    q='Create table if not exists abc(Sr_no int(4),name varchar(30),password varchar(30),age int(3),email varchar(30),mobile_no int(10),uid varchar(30))'
    cur.execute(q)
    q="Select max(sr_no)from abc"
    cur.execute(q)
    record=cur.fetchone()
    if(record[0]==None):
        sr_no=1
    else:
        sr_no=record[0]+1
    q="insert into abc values(%d,'%s','%s',%d,'%s','%s','%s')"%(sr_no,a,b,c,d,e,uid)
    cur.execute(q)
    con.commit()
    print('Your ID has been created successfully...')
def login_2():
    import pymysql as sq
    con=sq.connect('localhost','root','1234','abc')
    cur=con.cursor()
    q='Select uid from abc'
    cur.execute(q)
    record=cur.fetchall()
    for i in record:
      if(a==i[0]):
        print('processing...')
        break
      else:
        print('User not found')
        break
    q='Select password from abc'
    cur.execute(q)
    rec=cur.fetchall()
    for j in rec:
      if(b==j[0]):
        print('You have login successfully...')
        break
      else:
        print('Enter a valid UID & password')
        break
def prop():
    sr_no=0
    import pymysql as sq
    import warnings as wa
    wa.filterwarnings(action='ignore')
    con=sq.connect('localhost','root','1234','abc')
    cur=con.cursor()
    q="create table if not exists properties(Sr_no int(10),TOP varchar(10),BHK varchar(5),floors varchar(2),price int(20),location varchar(50),size varchar(15),fid varchar(20))"
    cur.execute(q)
    q='Select Max(Sr_no) from properties'
    cur.execute(q)
    record=cur.fetchone()
    if(record[0]==None):
        sr_no=1
    else:
        sr_no=record[0]+1
    fid=str(sr_no)+'_'+a+'_'+e
    print('Your fid is ',fid)
    q="insert into properties values(%d,'%s','%s','%s',%d,'%s','%s','%s')"%(sr_no,a,b,c,d,e,f,fid)
    cur.execute(q)
    con.commit()
def upd_prop():
    import pymysql as sq
    con=sq.connect('localhost','root','1234','abc')
    cur=con.cursor()
    q='Select fid from properties'
    cur.execute(q)
    record=cur.fetchall()
    for i in record:
      if(z==i[0]):
        print('you have login successfully...')
        break
      else:
        print('property not found')
        break
def upd_prop1():
    global z,a
    import pymysql as sq
    con=sq.connect('localhost','root','1234','abc')
    cur=con.cursor()
    q="update properties set price=%d where fid='%s'"%(a,z)
    cur.execute(q)
    con.commit()
def del_prop():
    import pymysql as sq
    con=sq.connect('localhost','root','1234','abc')
    cur=con.cursor()
    q="Delete from properties where fid='%s'"%(z)
    cur.execute(q)
    con.commit()
    print('Your record have been deleted successfully...')
def show_prop():
    import pymysql as sq
    con=sq.connect('localhost','root','1234','abc')
    cur=con.cursor()
    q='Select * from properties'
    cur.execute(q)
    record=cur.fetchall()
    for x in record:
        print(x,'\n')
def app():
    sr_no=0
    import pymysql as sq
    import warnings as wa
    wa.filterwarnings(action='ignore')
    con=sq.connect('localhost','root','1234','abc')
    cur=con.cursor()
    q="create table if not exists appointments(Sr_no int(10),uid varchar(20),fid varchar(20),Adate date)"
    cur.execute(q)
    q='Select Max(Sr_no) from appointments'
    cur.execute(q)
    record=cur.fetchone()
    if(record[0]==None):
        sr_no=1
    else:
        sr_no=record[0]+1
    aid=str(sr_no)+'_'+a+'_'+z
    print('Your aid is ',aid)
    q="insert into appointments values(%d,'%s','%s','%s')"%(sr_no,a,z,w)
    cur.execute(q)
    con.commit()
    
x=int(input('Press\n1.Login as User\n2.Login as Admin\n=>'))
if(x==1):
    y=int(input('Press\n1.New user\n2.Existing user\n=>'))
    if(y==1):
        a=input('Enter your name ')
        b=input('Enter your password ')
        c=int(input('Enter your age '))   
        def inv():
            if(len(c)<2 and len(c)>3):
                c=int(input('Enter a valid age '))
            if(type(c)!=int):
                c=int(input('Enter a valid age '))
        inv()
        d=input('Enter your E-mail ID ')
        e=input('Enter your mobile no. ')
        def inv_2():
            if(e<10 and e>10):
                e=input('Enter a valid 10 digit phone no.')
        inv_2()
        uid=a+'_'+str(c)+'_'+e
        print('Your user ID is ',uid) 
        login()
    elif(y==2):
        a=input('Enter your user ID ')
        b=input('Enter your password ')
        login_2()
        show_prop()
        c=input('Do you want buy any property(y/n)\n=>')
        if(c=='y' or c=='Y'):
            w=input('Give a date for appointment(yyyy-mm-dd) ')
            z=input('Enter fid of property you want to buy\n=>')
            app()
        elif(c=='n'or c=='N'):
            print('Thanks for visiting...')
                
elif(x==2):
    y=int(input('Press\n1.To insert record\n2.To update record\n3.To delete record\n4.See all records\n=>'))
    if(y==1):
        a=input('Enter type of property ')
        b=input('Enter BHK ')
        c=input('Enter no. of floors ')
        d=int(input('Enter price '))
        e=input('Enter location ')
        f=input('Enter size(in hectares)')
        prop()
        print('Your record has been inserted successfully...')
    elif(y==2):
        z=input('Enter fid of property ')
        upd_prop()
        a=int(input('Enter new price of property '))
        upd_prop1()
        print('Your record have been updated successfully...')
    elif(y==3):
        z=input('Enter fid of property ')
        upd_prop()
        a=input('Do you want delete this record(y/n)\n=>')
        if(a=='y' or a=='Y'):
            del_prop()
        elif(a=='n' or a=='N'):
            print('Thank you')
    elif(y==4):
        show_prop()
        


        
