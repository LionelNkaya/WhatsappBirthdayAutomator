'''
This programs looks in the database and returns each friend_name for which friend_DOB = today

Credit:
How to use python variables in sqlite select query: https://www.youtube.com/watch?v=pd-0G0MigUA&t=1200s
'''

import sqlite3
from datetime import date

#Creating connection to DB
connection = sqlite3.connect("sqlite_App.db")
cursor = connection.cursor()

today = str(date.today().strftime('%m-%d'))
friends = []

# correct query: select friend_name from friends where friend_DOB LIKE "%-04-15";

def birthday_checker():
    # Check in the column friend_DOB if a date matches today
    for row in cursor.execute("select friend_name from friends where friend_DOB = :dob", {'dob': today}) : 
        friend_name = ""
        for element in row: # Because row is a tuple I have to convert it to a string to get the friend name
            friend_name = friend_name + element
            
        friends.append(friend_name)
    return friends



