print("*"*90)
print("\t\t\t\tPAYROLL MANAGEMENT SYSTEM")
print("*"*90)

#creating database
import mysql.connector as con
c=con.connect(host="localhost", user="root", passwd="123456")           
cur=c.cursor()
query="Create database if not exists payroll"
cur.execute(query)
cur.execute("Use payroll")

#creating table
sql="Create table if not exists emp(EmpNo int primary key,Name varchar(20) not null,Post varchar\
(15),BasicSalary int,DA float,HRA float, GrossSalary float,Tax float,NetSalary float)"
cur.execute(sql)
c.commit()

while True:
    print()
    print()
    print("*"*90)
    print("\t\t\t\t\tMAIN MENU")
    print("*"*90)
    print()
    print("Press any number from 1 to 10 to execute any of the desired procedures given below")
    print()
    print("\t1: To Add Employee Records")
    print("\t2: To Display Records of All the Employees")
    print("\t3: To Display Record of a Particular Employee")
    print("\t4: To Delete Record of Particular Employee")
    print("\t5: To Display Payroll")
    print("\t6: To Increase an Employee's Salary")
    print("\t7: To Display Salary Slip of a Particular Employee")
    print("\t8: To Modify a Record")
    print("\t9: To Exit")
    print()
    ch=int(input('Enter Your Choice:'))
    
#Procedure to Add Employees
    if ch==1:
        print("Enter Employee Information......")
        eno=int(input("Enter EmpNo.:"))
        ename=input("Enter Employee's Name:")
        epost=input("Enter Employee's Post:")
        ebasic=float(input("Enter Employee's Basic Salary:"))
        if epost.upper()=='OFFICER':
            eda=ebasic*0.5
            ehra=ebasic*0.35
            etax=ebasic*0.2
        elif epost.lower()=='manager':
            eda=ebasic*0.45
            ehra=ebasic*0.30
            etax=ebasic*0.15
        else:
            eda=ebasic*0.40
            ehra=ebasic*0.25
            etax=ebasic*0.1
        egross=ebasic+eda+ehra
        enet=egross-etax
        sec=(eno,ename,epost,ebasic,eda,ehra,egross,etax,enet)
        S="insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(S,sec)
        c.commit()
        print("RECORDS ADDED SUCCESSFULLY !!!!!!!")
        print()

#Procedure to Display Records of All Employees        
    elif ch==2:
        S="Select * from emp"
        cur.execute(S)
        data=cur.fetchall()
        for i in data:
            print(i)
        print()

#Procedure to Display Records of A Particular Employee         
    elif ch==3:
        empno=int(input("Enter Emp No.:"))
        S="Select * from emp where EmpNo=%s"%(empno)
        cur.execute(S)
        data=cur.fetchone()
        if data==None:
            print("Record not found")
            print()
            print("*"*90)
        else:
            print(data)
            print()
                
#Procedure to Delete Record of A Particular Employee                
    elif ch==4:
        try:
            empno=int(input("Enter Emp No.:"))
            S="Delete from emp where EmpNo=%s"%(empno)
            cur.execute(S)
            c.commit()
            print("Record Deleted Successfully !!!!!")
            c.commit()
            print()
        except:
            print("Something Went Wrong !!!!!")
            print()

#Procedure To Display Payroll            
    elif ch==5:
        S="Select * from emp"
        cur.execute(S)
        data=cur.fetchall()
        print("*"*100)
        print("PAYROLL".center(90))
        print("*"*100)
        print("| EmpNo |  Name   |  Post   | BasicSalary |    DA     |   HRA   | GrossSalary |  Tax   | NetSalary |")
        for i in data:
            print("|  ",i[0],"  | ",i[1]," |",i[2],"|   ",i[3],"   | ",i[4]," |",i[5],"|  ",i[6],"  |",i[7],"| ",i[8]," |")
        print()

#Procedure to Increase The Salary of An Employee        
    elif ch==6:
        amt=int(input("Enter amount of salary to be increased:"))
        eno=int(input("Enter Emp No.:"))
        cur.execute("Select * from emp")
        d=cur.fetchall()
        for i in d:
            if  i[0]==eno:
                cur.execute("Select * from emp where EmpNo=%s"%(eno))
                data=cur.fetchone()
                t=data[3]+amt
                if data[2].upper()=='OFFICER':
                    da=t*0.5
                    hra=t*0.35
                    tax=t*0.2
                elif data[2].lower()=='manager':
                    da=t*0.45
                    hra=t*0.30
                    tax=t*0.15
                else:
                    da=t*0.40
                    hra=t*0.25
                    tax=t*0.1
                g=t+da+hra
                n=g-tax
                cur.execute("Update emp set BasicSalary=%s,DA=%s,HRA=%s,GrossSalary=%s,Tax=%s,NetSalary=%s where EmpNo='%s'"%(t,da,hra,g,tax,n,eno))
                c.commit()
                print("Updated Successfully !!!!!!!")
                print()
                n=1
                break
        if n!=1:
            print("Record Not Found !!!!!")
            print()
#Procedure to Display Salary Slip of A Particular Employee            
    elif ch==7:
        eno=int(input("Enter Emp No. to display the Salary Slip:"))
        print()
        cur.execute("Select * from emp")
        d=cur.fetchall()
        for i in d:
            if i[0]==eno:
                print("*"*90)
                print("Salary Slip".center(90))
                print("*"*90)
                print()
                cur.execute("Select Name,BasicSalary,DA,HRA,Tax,NetSalary from emp where EmpNo=%s"%(eno,))
                d=cur.fetchone()
                print("-------------------------")
                print("|    Name    :",d[0],"   |")
                print("|Basic Salary:",d[1],"   |")
                print("|     DA     :",d[2]," |")
                print("|     HRA    :",d[3]," |")
                print("|     Tax    :",d[4],"  |")
                print("| Net Salary :",d[5]," |")
                print("-------------------------")
                print()
                n=1
                break
            else:
                n=2
        if n==2:
            print("Record Not Found !!!!!")
            print()

#Procedure to Modify A Record            
    elif ch==8:
        eno=int(input("Enter Emp No. Whose Record Is To Be Modified:"))
        cur.execute("Select * from emp")
        data=cur.fetchall()
        for i in data:
            if i[0]==eno:
                cur.execute("Select * from emp where EmpNo=%s"%(eno))
                d=cur.fetchone()
                ename=d[1]
                epost=d[2]
                ebasic=d[3]
                eda=d[4]
                ehra=d[5]
                eg=d[6]
                etax=d[7]
                en=d[8]
                print("Empolyee Id         :",d[0])
                print("Name                :",d[1])
                print("Post                :",d[2])
                print("Basic Salary        :",d[3])
                print("Dearing Allowance   :",d[4])
                print("House Rent Allowance:",d[5])
                print("Gross Salary        :",d[6])
                print("Tax                 :",d[7])
                print("Net Salary          :",d[8])
                print("-"*45)
                print("Enter Value To Modify Below or Just Press Enter For No Change...")
                x=input("Enter Name:")
                if len(x)>0:
                    ename=x
                x=input("Enter Post:")
                if len(x)>0:
                    epost=x
                    if epost.upper()=='OFFICER':
                        eda=ebasic*0.5
                        ehra=ebasic*0.35
                        etax=ebasic*0.2
                    elif epost.lower()=='manager':
                        eda=ebasic*0.45
                        ehra=ebasic*0.30
                        etax=ebasic*0.15
                    else:
                        eda=ebasic*0.40
                        ehra=ebasic*0.25
                        etax=ebasic*0.1
                    eg=ebasic+eda+ehra
                    en=eg-etax
                x=input("Enter Basic Salary:")
                if len(x)>0:
                    ebasic=float(x)
                    if epost.upper()=='OFFICER':
                        eda=ebasic*0.5
                        ehra=ebasic*0.35
                        etax=ebasic*0.2
                    elif epost.lower()=='manager':
                        eda=ebasic*0.45
                        ehra=ebasic*0.30
                        etax=ebasic*0.15
                    else:
                        eda=ebasic*0.40
                        ehra=ebasic*0.25
                        etax=ebasic*0.1
                    eg=ebasic+eda+ehra
                    en=eg-etax
                pes=(ename,epost,ebasic,eda,ehra,eg,etax,en,eno)
                S="Update emp set Name='%s',Post='%s',BasicSalary=%s,DA=%s,HRA=%s,GrossSalary=%s,Tax=%s,NetSalary=%s where EmpNo=%s"%(pes)
                print("Records Modified Sucessfully !!!!!")
                cur.execute(S)
                c.commit()
                n=1
                break
        if n!=1:
            print("Record Not Found !!!!!")

#Procedure To Exit                
    elif ch==9:
        print()
        print("-X"*50)
        break
    
    else:
        print("Wrong Input !!!!!")
