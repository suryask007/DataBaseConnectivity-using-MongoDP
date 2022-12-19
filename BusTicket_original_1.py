from database import *
from datetime import date as dt
import datetime
import random as ra
import re
p=int(input("Enter the phone number:"))
m=p
count=0
sum1=0
while m!=0:
    count+=1
    d=m%10
    sum1=sum1+d
    m//=10
if count==10:
    class bus():
        def __init__(self,b_no,b_name,phone=p):
            self.b_no=b_no
            self.b_name=b_name
            self.phone=phone
        def details(self):
            print("your BUS NUMBER is :",self.b_no)
            print("your BUS NAME is:",self.b_name)
            print("your Phone Number is:",self.phone)
            print("This Bus from \t<-><-><->\tChennai to COIMBATORE\t<-><-><->")
            print("Your Stops are :\n\t 1.Villupuram \n\t 2.Salem \n\t 3.Coimbatore \n\t 4.Villu_details \n\t 5.salem_details \n\t 6.Cbe_details")
            c.insert_details(self.b_name,self.phone,self.b_no)
        def Villupuram(self,km=166.3,amount=160):
            print("you are selected VILLUPURAM ")
            count=0
            user4=int(input("How Many Passenger are travel:" ))
            for i in range(0,user4):
                count+=1
                user1=str(input("Enter the Passenger Name:"))
                print("please Enter your Date of Birth:")
                year=int(input("enter the year:"))
                month=int(input("enter the month:"))
                day=int(input("enter the date:"))
                DOB=dt(year,month,day)
                today=dt.today()
                age=today.year-DOB.year-((today.month,today.day)<(DOB.month,DOB.day))
                print(f"You have Entered Details are is: \n\tNAME--->{user1}\n\tPHONE NUMBER--->{self.phone}\n\tYour DOB is--->{DOB}\n\tYour age is --->{age}")
                date_time=datetime.datetime.now()
                c.insert_details_travel(user1,self.phone,age,user4,date_time)
                

            upi=input("enter the UPI ID:")
            con=re.compile("^[a-zA-Z0-9]+\@[a-z]+\.[a-z]+$")
            if con.search(upi):
                ran=ra.randrange(1000,9999)
                print(ran)
                user=int(input(f"Enter the OTP you Have Recivied  :"))
                if user==ran:
                    print("\t***Your OTP is matched***")
                    print(f"you have booked for {count}  members")
                    print(f"Chennai TO Villupuram km {km} and Amount of one person is {amount} and {count} person is {count*amount}")
                    date_time=datetime.datetime.now()
                    print(f"\t###YOU Have Booked Succesfully### on {date_time}")
                    print(f"\tTHANK YOU For Visiting Us {self.b_name}")
                    
                else:
                    print("\t!!!your OTP is MISS MATCH!!!")
                
            else:
                print("\tplease Enter the Correct UPI ID")
            
            
        def salem(self,km=344.5,amount=350):
            user=int(input("How Many Passenger are travel:" ))
            count=0
            for i in range(0,user):
                count+=1
                print("you are selected Salem ")
                user1=str(input("Enter the Passenger Name:"))
                print("please Enter your Date of Birth:")
                year=int(input("enter the year:"))
                month=int(input("enter the month:"))
                day=int(input("enter the date:"))
                DOB=dt(year,month,day)
                today=dt.today()
                age=today.year-DOB.year-((today.month,today.day)<(DOB.month,DOB.day))
                print(f"You have Entered Details are is: \n\tNAME--->{user1}\n\tPHONE NUMBER--->{self.phone}\n\tYour DOB is--->{DOB}\n\tYour age is --->{age}")
                date_time=datetime.datetime.now()
                c.insert_salem(user1,self.phone,age,user,date_time)
            upi=input("enter the UPI ID:")
            #c_upi=input("enter the UPI ID:")
            con=re.compile("^[a-zA-Z0-9]+\@[a-z]+\.[a-z]+$")
            if con.search(upi):
                ran=ra.randrange(1000,9999)
                print(ran)
                user=int(input(f"Enter the OTP you Have Recivied  :"))
                if user==ran:
                    print("\t***Your OTP is matched***")
                    print(f"you have booked for {count}  members")
                    print(f"Chennai TO Salem km {km} and Amount of one person is {amount} and {count} person is {count*amount}")
                    date_time=datetime.datetime.now()
                    print(f"\t###YOU Have Booked Succesfully### on {date_time}")
                    print(f"\tTHANK YOU For Visiting Us {self.b_name}")
                else:
                    print("\t!!!your OTP is MISS MATCH!!!")
            else:
                print("\tEnter the Correct UPI ID")
            
        def Coimbatore(self,km=505.5,amount=600):
            user=int(input("How Many Passenger are travel:" ))
            count=0
            for i in range(0,user):
                count+=1
                print("you are selected Coimbatore ")
                user1=str(input("Enter the Passenger Name:"))
                print("please Enter your Date of Birth:")
                year=int(input("enter the year:"))
                month=int(input("enter the month:"))
                day=int(input("enter the date:"))
                DOB=dt(year,month,day)
                today=dt.today()
                age=today.year-DOB.year-((today.month,today.day)<(DOB.month,DOB.day))
                print(f"You have Entered Details are is: \n\tNAME--->{user1}\n\tPHONE NUMBER--->{self.phone}\n\tYour DOB is--->{DOB}\n\tYour age is --->{age}")
                date_time=datetime.datetime.now()
                c.insert_cbe(user1,self.phone,age,user,date_time)
            upi=input("enter the UPI ID:")
            con=re.compile("^[a-zA-Z0-9]+\@[a-z]+\.[a-z]+$")
            if con.search(upi):
                ran=ra.randrange(1000,9999)
                print(ran)
                user=int(input(f"Enter the OTP you Have Recivied  :"))
                if user==ran:
                    print("\t***Your OTP is matched***")
                    print(f"you have booked for {count}  members")
                    print(f"Chennai TO Coimbatore km {km} and Amount of one person is {amount} and {count} person is {count*amount}")
                    date_time=datetime.datetime.now()
                    print(f"\t###YOU Have Booked Succesfully### on {date_time}")
                    print(f"\tTHANK YOU For Visiting Us {self.b_name}")
                else:
                    print("\t!!!your OTP is MISS MATCH!!!")
            else:
                print("\tEnter the Correct UPI ID")
            
        def main(self):
            user=int(input("Enter the Option to Continue:"))
            if user==1:
                M.Villupuram()
            elif user==2:
                M.salem()
            elif user==3:
                M.Coimbatore()
            elif user==4:
                name=str(input("Enter the name to find:"))
                c.get_villupuram(name)
            elif user==5:
                name=str(input("Enter the name to be find:"))
                c.get_salem(name)
                
            elif user==6:
                name=str(input("Enter the name to be find:"))
                c.get_cbe(name)
            else:
                print("!!!Enter above the option only!!!")
    M=bus("TN25 AA 2001","SURYA TRAVELS")
    M.details()
    M.main()
else:
    print("Enter the Correct 10 Digths Phone Number")
            

                
