'''
Creating a file connecting to sqlite 3 db to allow user to add data to db. 
The schema of the table is going to be the following: 
table name: friends
friend_name: string
friend_DOB: string
'''
import sqlite3
import datetime

#Creating connection to DB
connection = sqlite3.connect("app.db")
cursor = connection.cursor()

#Command used to create table
#cursor.execute('''CREATE TABLE friends(friend_name TEXT, friend_DOB TEXT)''')



def adding_friend_to_DB() :
    # Capturing name and date of birth

    friend_name = input('Enter friend name ')
    #year = int(input('Enter a year '))
    month = int(input('Enter a month '))
    if month < 10:
        month = f"0{month}"
    day = int(input('Enter a day '))
    if day < 10:
        day = f"0{day}"
    DOB_user = f"{month}-{day}"

    # Writing name and date of birth to db

    cursor.execute("INSERT INTO friends VALUES (?,?)", (friend_name, DOB_user))
    connection.commit()

    # Asking the user if he/she wants to add a friend by calling the add frined to db function again
    decision= input("Friend added successfully. Do you want to add another friend? Y / N ")
    if decision == 'Y':
        adding_friend_to_DB()
    else:
        print("Thank you for adding a friend to the app. Goodbye.")    



adding_friend_to_DB()
connection.close()