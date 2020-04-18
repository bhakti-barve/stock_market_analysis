import pymongo
import datetime
import pandas as pd
from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.library

def display():
   doc = [i for i in db.Book.find()]
   table = pd.DataFrame(doc)
   print(table)

def search_genre():
   print("Searching books by genres:")
   ch='y'
   while(ch=='y'):
      print("\nBook Genres:")
      print("\n1.Science Fiction\n2.Thriller")
      choice=int(input("Enter the book genre:"))
      if(choice==1):
         print("Books available:")
         doc = [i for i in db.Book.find({'Genres':'Science Fiction','Status':'Available'})]
         table = pd.DataFrame(doc)
         print(table)
      ch=input("Do you wanna continue(y/n)?")

def search_book():
   print("Searching random book:")
   x=input("Enter book name:")
   if(db.Book.find({'BookName':x})):
      print("Book's info:")
      doc = [i for i in db.Book.find({'BookName':x})]
      table = pd.DataFrame(doc)
      print(table)

def stud_info():
   doc = [i for i in db.studInfo.find()]
   table = pd.DataFrame(doc)
   print(table)

def insert():
   a=int(input("Enter the student id:"))
   b=input("Enter the student name:")
   c=input("Enter the you want to take:")
   d=datetime.datetime.today()
   e= d+ datetime.timedelta(days = 30)
   if(db.Book.find({'BookName':c,'Status':'Available'}).count()==1 and db.Users.find({'id':a,'StudName':b}).count()==1):
     db.studInfo.insert([{'Id':a,'StudentName':b,'BookTaken':c,'IssueDate':d,'ReturnDate':e}])
   else:
      print("You are not Registered or Book is not available")
   doc = [i for i in db.studInfo.find()]
   table = pd.DataFrame(doc)
   print(table)

def fine():
   d=datetime.datetime.today()
   db.studInfo.aggregate([ { '$project': { 'Name': '$StudentName', 'fine': { '$multiply':[ {'$trunc': { '$divide': [{ '$subtract': [ d, '$ReturnDate'] }, 1000 * 60 * 60 * 24] } } , 2 ] } } }, { '$out':'Fine'} ] )
   doc = [i for i in db.Fine.find({'fine':{ '$gt': 0 }})]
   table = pd.DataFrame(doc)
   print(table)

def Register():
   print("REGISTRATION:")
   a=int(input("Enter your new id(to get register) :"))
   b=input("Enter your Name :")
   db.Users.insert({'id':a,'StudName':b})
   doc = [i for i in db.Users.find()]
   table = pd.DataFrame(doc)
   print(table)

def edit():
   print("EDITING STUDENT INFO:")
   a=int(input("Enter the id to edit:"))
   b=input("Enter new name:")
   db.Users.update({"id":a},{"$set":{"StudName":b}})
   doc = [i for i in db.Users.find()]
   table = pd.DataFrame(doc)
   print(table)




#edit()
#Register()
display() 
#search_book()
#search_genre()
#fine()
#insert()

