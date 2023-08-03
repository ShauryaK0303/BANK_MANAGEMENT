#PROJECT  ON BANK_MANAGEMENT_SYSTEM                     #UNION_OVERSEAS_BANK
#----------------------------------------------------------------------------------------
loginvalue=False
print('\n\n************************UNION OVERSEAS BANK******************************')
print('\n\n')
IDD=None
import mysql.connector as m
import random
Password=input('Enter your mysql password: ')
import time

t0 = time.time()
def install(i):# INSTALLATION TIME OF THE DATABASE
    t1 = time.time()
    print("Installation progress({}%)".format(100*i//40))
    
db=m.connect(host='localhost',user='root',passwd="{}".format(Password),auth_plugin='\
mysql_native_password')
cur=db.cursor()
cur.execute('show databases')
dat=cur
value=False
for i in dat:
    i=str(i[0])
    if i=='union_overseas_bank':#CHECKING IF THE DATABASE ALREADY EXISTS OR NOT
        value=True
        break
if value==False:# INSTALLING THE DATABASE USING THE CODE GIVEN BELOW
    print('\n\nINSTALLING DATABASE...\n')
    
    
    cur.execute('create database union_overseas_bank')
    install(1)
    cur.execute('use union_overseas_bank')
    install(2)
    query='create table login(user_id integer not null primary key,\
name varchar(60),password varchar(50) not null)'
    cur.execute(query)
    install(3)
    cur.execute("insert into login values(19906,'Mayank','mj')")
    install(4)
    cur.execute("insert into login values(19908,'shaurya','sk')")
    install(5)
    cur.execute("insert into login values(103,'kshitij','kg')")
    install(6)
    cur.execute("insert into login values(104,'aditya','aj')")
    install(7)
    cur.execute("insert into login values(105,'akshat','aj')")
    install(8)
    cur.execute('create table personal(CUS_ID int primary key,\
NAME varchar(80),ADDRESS varchar(120),COUNTRY varchar(20),ACC_NO int)')
    install(9)
    cur.execute('create table account_details(acc_no int primary key,acc_type \
varchar(40),balance int,last_transaction int,transaction_type varchar(10),\
transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
    install(10)
    cur.execute("insert into personal values(200904,'Gupta,Mahendra','\
B-421,Street No.-2,lajpat nagar,delhi','India',1500655723)")
    install(11)
    cur.execute("insert into account_details values(1500655723,'\
FIXED DEPOSIT',233094,9899,'DEBIT',default)")
    install(12)
    cur.execute("insert into personal values(210833,'PAWAR,RAJENDAR','b-213,\
street No.6,Shivaji Nagar,Nagpur','India',1600983402)")
    install(13)
    cur.execute("insert into account_details values(1600983402,'SAVINGS',\
133240,2900,'DEBIT',default)")
    install(14)
    cur.execute("insert into personal values(210344,'BROOK,RICHARD','\
1442,Kensington street,seattle','U.S.A',1540995620)")
    install(15)
    cur.execute("insert into account_details values(1540995620,'RECURRING DEPOSIT',\
344020,3000,'DEBIT',default)")
    install(16)
    cur.execute("insert into personal values(232665,'SHARMA,RAMKAUMAR',\
'524,Peeragadhi,Nangloi','INDIA',1670884329)")
    install(17)
    cur.execute("insert into account_details values(1670884329,'SALARY',\
514566,34450,'CREDIT',default)")
    install(18)
    cur.execute("insert into personal values(214643,'SINGH,MUKESH',\
'B-210,Street no.4,Vivek Vihar,delhi','INDIA',1400235348)")
    install(19)
    cur.execute("insert into account_details values(1400235348,\
'RECUURING DEPOSIT',211342,2300,'DEBIT',default)")
    install(20)
    cur.execute("insert into personal values(214655,'TODD,JAMES',\
'122b,baker street,London','UK',1682335409)")
    install(21)
    cur.execute("insert into account_details values(1682335409,'SALARY',\
248770,3500,'DEBIT',default)")
    install(22)
    cur.execute('insert into personal values(200829,"FOX,LUCIUS","1563,Forrest \
avenue,kingston,ENGLAND","UK",1500302088)')
    install(23)
    cur.execute("insert into account_details values(1500302088,'OVER DRAFT',\
13454555,4556,'CREDIT',DEFAULT)")
    install(24)
    cur.execute('insert into personal values(210255,"KUSHWAH,SHAURYA","b-12,\
ram nagar,delhi","india",1524447238)')
    install(25)
    cur.execute("insert into account_details values(1524447238,'CURRENT',\
13455624,55556,'CREDIT',DEFAULT)")
    install(26)
    cur.execute('insert into personal values(234453,"GAUTAM,KSHITIZ","456,LIG flats,\
ashok nagar,delhi","india",1525884338)')
    install(27)
    cur.execute("insert into account_details values(1525884338,'SAVINGS',\
2454555,23323,'CREDIT',DEFAULT)")
    install(28)
    cur.execute('insert into personal values(233418,"JAIN,ADITYA","c-4,yamuna vihar,delhi\
","india",1524568643)')
    install(29)
    cur.execute("insert into account_details values(1524568643,'OVER DRAFT',\
13454555,4556,'CREDIT',DEFAULT)")
    install(30)
    cur.execute('insert into personal values(215598,"KUMAR,AKSHAT","c1,bhajanpura,delhi\
","india",1570940057)')
    install(31)
    cur.execute("insert into account_details values(1570940057,'OVER DRAFT',\
45653555,5665,'DEBIT',DEFAULT)")
    install(32)
    cur.execute("create table transact(acc_no int,trans_amount int,trans_type \
varchar(20),time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    install(33)
    cur.execute("insert into transact values(1500302088,2000,'DEBIT',default)")
    install(34)
    cur.execute("insert into transact values(1500302088,2000,'DEBIT',default)")
    install(35)
    cur.execute("insert into transact values( 1600983402,40000,'DEBIT',default)")
    install(36)
    cur.execute("insert into transact values(1500655723,10000,'CREDIT',default)")
    install(37)
    cur.execute("insert into transact values(1400235348,21555,'CREDIT',default)")
    install(38)
    cur.execute("insert into transact values( 1570940057,35000,'DEBIT',default)")
    install(39)
    db.commit()
    install(40)
else:
    cur.execute('use union_overseas_bank')

def check(usrid):#CHECKING WHETHER A INSERTED ID EXISTS OR NOT
    
    'Checks whether user id exists or not'
    cur.execute('select user_id from login')
    uid=cur
    uid=uid.fetchall()
    uid=list(uid)
    sameuid=0
    for i in uid:
        i=int(i[0])
        if i==usrid:
            sameuid=i
            break
    if usrid==sameuid:
        print('\n User ID Exists')
        try:
            nusrid=int(input('Please enter new User ID:'))
        except ValueError:
            print()
            nusrid=int(input('Please enter new User ID in numeric form:'))
        check(nusrid)
        return nusrid
    elif sameuid==0:
        return usrid


def login(Id):#CHECKING FOR SAME USER IDs OR COUNTERFEIT ONES
    cur.execute('select user_id from login')
    usid=cur
    usid=usid.fetchall()
    usid=list(usid)
    sameusid=0
    for i in usid:
        i=int(i[0])
        if i==Id:
            sameusid=i
            break
    if sameusid==0:
        print('\nInvalid Login\n\n\n\n\n\n')
        quit()
    else:
        y=input('Enter Password: ')
        cur.execute('select password from login')
        pd=cur
        pd=pd.fetchall()
        pd=list(pd)
        samepd=0
        for i in pd:
            i=str(i[0])
            if i==y:
                samepd=i
                break
        if Id==sameusid and y==samepd:
            print('\nLogin Successful')
            'the code'
            global loginvalue
            loginvalue=True
        else:
            print('\nInvalid Login\n\n\n\n\n\n')
            quit()
print('\n\n')
x=int(input('Enter User ID: '))
if x in [19906,19908]:
    IDD=x
print('\n')
login(x)
#-------------------------------------------------------------------------------------------
def add_emp():# CREATING A NEW USER(SERVICE GRANTED TO ADMINS OF THE SERVER ONLY)
    print()
    try:
        n=int(input('Enter new  User ID: '))
    except ValueError:
        print('\nOps!')
        n=int(input('Please enter new User ID in numeric form: '))
    z=check(n)
    passw=input('Enter new password: ')
    passw1=input('\nConfirm password: ')
    if passw==passw1:
        name=input('\nEnter employee name: ')
        query="insert into login values(%s,'%s','%s')"%(z,name,passw)
        cur.execute(query)
        db.commit()
        print('Employee details generated successfully')
    elif passw!=passw1:
        while passw!=passw1:
            print('\n','#################################confirmation not matched############################'.swapcase(),'\n',sep='')
            passw=input('Enter new password: ')
            passw1=input('\nConfirm password: ')
        else:
            name=input('\nEnter employee name: ')
            query="insert into login values(%s,'%s','%s')"%(z,name,passw)
            cur.execute(query)
            db.commit()
            print('Employee details generated successfully\n')
#-----------------------------------------------------------------------------------
def user_id():#TO GENERATE A USER ID FOR NEW ACCOUNT
    cur.execute("select CUS_ID from personal")
    cuss=cur.fetchall()
    l=[]
    for i in cuss:
        l.append(i[0])
    ID=random.randint(200000,300000)
    while ID in l:
        ID=random.randint(200000,300000)
    return ID
#-------------------------------------------------------------------------------------
def acc_no():#TO GENERATE ACCOUNT NUMBER FOR NEW ACCOUNT
    cur.execute("select ACC_NO from personal")
    cus=cur.fetchall()
    Li=[]
    for i in cus:
        Li.append(i[0])
    ac=random.randint(1400000000,1900000000)
    while ac in Li:
        ac=random.randint(1400000000,1900000000)
    return ac
#----------------------------------------------------------------------------------
def inst():#TO MAKE NEW ACCOUNT
    run=True
    while run==True:
        nam=input("Enter the Name(SURNAME,FIRST NAME)::")
        pata=input("Enter permanent Address::")
        place=input("Enter Nationality::")
        ac_ty=input("Enter Account Type::")
        BAl=eval(input("Enter Opening Balance::"))
        Id=user_id()
        acc=acc_no()
        qu="insert into personal values({},'{}','{}','{}',{})".format(Id,nam,pata,place,acc)
        query="insert into account_details(ACC_NO,ACC_TYPE,BALANCE) values({},'{}',{})".format(acc,ac_ty,BAl)
        cur.execute(qu)
        db.commit()
        cur.execute(query)
        db.commit()
        ch=input("Do you wish to open more accounts?Enter yes/no::")
        print()
        if ch.lower() in 'y,yes':
            run=True
        if ch.lower() in 'n,no':
            run=False
        print("\nRECORD ENTERED SUCCESSFULLY!")
        print("\nYOUR CUSTOMER ID IS::",Id)
        print("\nYOUR ACCOUNT NUMBER IS::",acc)
#----------------------------------------------------------------------------------------------
def trans():#TO MAKE TRANSACTIONS IN A ACCOUNT
    r=True
    while r==True:
        A=int(input("Enter Account Number::"))
        cur.execute("select acc_no from account_details")
        cus=cur.fetchall()
        Li=[]
        for i in cus:
            Li.append(i[0])
        if A in Li:
            ty=input("Enter Transaction Type(DEBIT,CREDIT)::")
            ty=ty.upper()
            am=int(input("Enter transaction Amount::"))
            cur.execute("insert into TRANSACT values({},{},'{}',default)".format(A,am,ty))
            db.commit()
            if ty=="DEBIT":
                cur.execute("update account_details set BALANCE=BALANCE-{} where ACC_NO={}".format(am,A))
                db.commit()
            elif ty=="CREDIT":
                cur.execute("update account_details set BALANCE=BALANCE+{} where ACC_NO={}".format(am,A))
                db.commit()
            cur.execute("update account_details set TRANSACTION_TYPE='{}' where ACC_NO={}".format(ty,A))
            db.commit()
            cur.execute("update account_details set LAST_TRANSACTION={} where ACC_NO={}".format(am,A))
            db.commit()
            cur.execute("update account_details set TRANSACTION_TIME=default where ACC_NO={}".format(A))
            db.commit()
            print('TRANSACTION TRAVERSED SUCCESSFULLY!')
        else:
            print("No such account Exists.Please try Again.")
        wi=input("Do you wish to make more transactions?Enter yes/no::")
        print()
        if wi.lower() in 'y,yes':
            r=True
        if wi.lower() in 'n,no':
            r=False
#--------------------------------------------------------------------------------------------------
def pers_updt():#TO UPDATE ACCOUNT KYC
    RUN=True
    while RUN==True:
        Cu=int(input("Enter Customer ID::"))
        cur.execute("select CUS_ID from personal")
        cus=cur.fetchall()
        Li=[]
        for i in cus:
            Li.append(i[0])
        if Cu in Li:
            cur.execute("select * from personal where CUS_ID={}".format(Cu))
            Cus=cur.fetchall()
            L=[]
            for i in Cus[0]:
                L.append(i)
            print("\nRECORD FOUND!- DETAILS:")
            print('CUSTOMER ID',L[0],sep=':')
            print("ACCOUNT NUMBER",L[4],sep=":")
            print("NAME",L[1],sep=":")
            print("ADDRESS",L[2],sep=":")
            print("COUNTRY",L[3],sep=":")
            print()
            nam=input("Enter  New Name::")
            pat=input("Enter New Address::")
            pla=input("Enter New Country::")
            cur.execute("update personal set NAME='{}',COUNTRY='{}',ADDRESS='{}' where CUS_ID={}".format(nam,pla,pat,Cu))
            db.commit()
            print("\nRECORD UPDATED SUCCESSFULLY!")
        else:
            print("No record exists with respect to this customer Id.")

        wi=input("Do you wish to update any more records?Enter yes/no::")
        print()
        if wi.lower() in 'y,yes':
            RUN=True
        if wi.lower() in 'n,no':
            RUN=False
#-------------------------------------------------------------------------------------------       
def passbook():#TO FETCH PASSBOOK OF A ACCOUNT
    ac=int(input("Enter The Account Number::"))
    cur.execute("select acc_no from account_details")
    cus=cur.fetchall()
    Li=[]
    for i in cus:
        Li.append(i[0])
    if ac in Li:
        print("\n****** UNION_OVERSEAS_BANK ******\n \t\tPASSBOOK\n\t")
        cur.execute("select CUS_ID,NAME,ACC_NO,ACC_TYPE,BALANCE,ADDRESS,COUNTRY \
from personal natural join account_details where ACC_NO={}".format(ac))
        cu=cur.fetchall()
        name=cu[0][1].split(',')
        print("CUSTOMER ID::",cu[0][0],'\nNAME::',name[1],name[0],'\nACCOUNT \
NUMBER::',cu[0][2],'\nACCOUNT TYPE::',cu[0][3],'\nBALANCE::',cu[0][4],'\nADDRESS::\
',cu[0][5],'\nCOUNTRY::',cu[0][6])
        print()
        print("{:<20}{:<20}{:<20}{:<20}".format("ACCOUNT NUMBER","TRANSACTION \
TIME","TRANSACTION AMOUNT","TRANSACTION TYPE"))
        cur.execute("select * from TRANSACT")
        dat=cur.fetchall()
        if len(dat)>0:
            print()
            cur.execute("select ACC_NO,time,trans_amount,trans_type \
from transact where ACC_NO={}".format(ac))
            d=cur.fetchall()
            for i in d:
                print("{:<20}{:<30}{:<20}{:<20}".format(i[0],str(i[1]),i[2],i[3]))
        else:
            print("NO TRANSACTION MADE UNTIL NOW.")
    else:
        print("No Such account exists. Please try again.")
#--------------------------------------------------------------------------------------------
def delete():#TO CLOSE AN ACCOUNT
    ru=True
    while ru==True:
        acc=int(input("Enter Account Number(TO BE CLOSED)::"))
        cur.execute("select acc_no from account_details")
        cus=cur.fetchall()
        Li=[]
        for i in cus:
            Li.append(i[0])
        if acc in Li:
            conf=input("DO YOU REALLY WISH TO CLOSE THE ACCOUNT? ENTER YES?NO::")
            if conf.lower() in 'y,yes':
                cur.execute("delete from personal where ACC_NO={}".format(acc))
                cur.execute("delete from account_details where ACC_NO={}".format(acc))
                cur.execute("delete from transact where ACC_NO={}".format(acc))
                db.commit()
                print("\nACCOUNT CLOSED SUCCESSFULLY!.")
            else:
                print("\nNO UPDATION MADE.")
        else:
            print("\nNo Such account exists. Please try again.")
        wi=input("Do you wish to close anymore accounts ?Enter yes/no::")
        print()
        if wi.lower() in 'y,yes':
            ru=True
        if wi.lower() in 'n,no':
            ru=False
#--------------------------------------------------------------------------------------------
#MAIN MENU,COMPRISING ALL THE POSSIBLE OPTIONS AVAILABLE TO THE USER.IF A USER IS THE ADMIN OF
#BANK, IT GRANTS HIM AN EXTRA AUTHORITY OF BEING ABLE TO REGISTER A NEW USER.BUT AN ORDINARY
#USER OR EMPLOYEE IS NOT ABLE TO DO SO.
RUUN=False
if loginvalue==True:
    RUUN=True
if RUUN==True:
    print("************************WELCOME TO UNION OVERSEAS BANK*************************")
    print("\n**************************CONNECTION ESTABLISHED*******************************")
while RUUN==True:
    print()
    if IDD in [19906,19908]:
        print('WELCOME SIR..\n')
        print("\n1.OPEN NEW ACCOUNT",'\n2.UPDATE ACCOUNT DETAILS','\n3.INSERT TRANSACTION\
','\n4.GENERATE PASSBOOK','\n5. CLOSE AN ACCOUNT','\n6.ADD NEW EMPLOYEE\n')
    else:
        print("\n1.OPEN NEW ACCOUNT",'\n2.UPDATE ACCOUNT DETAILS','\n3.INSERT TRANSACTION\
','\n4.GENERATE PASSBOOK','\n5. CLOSE AN ACCOUNT\n')
    cho=str(input("ENTER YOUR CHOICE:"))
    if cho=='1':
        inst()
    elif cho=='2':
        pers_updt()
    elif cho=='3':
        trans()
    elif cho=='4':
        print()
        passbook()
    elif cho=='5':
        delete()
    elif cho=='6' and IDD in [19906,19908]:
        add_emp()
    else:
        print("No such choice exists.")
        RUUN=False
    wi=input("\nDo you wish to continue?Enter yes/no::")
    if wi.lower() in 'y,yes':
        RUUN=True
    elif wi.lower() in 'n,no':
        RUUN=False
#-----------------------------------------------------------------------------------------------
# CREATED BY:
#SHAURYA KUSHWAH XII-A
#UNDER THE GUIDANCE AND DIRECTIONS OF Ms. SEEMA SHARMA

