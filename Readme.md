# Whatsapp Birthday Automator

This project is insipired from a project developed by [The Assembly](http://members.theassembly.ae/index).
Link to the YouTube video tutorial is available [here](https://www.youtube.com/watch?v=eela1UYObWE&t=997s)

This program allows user to add friends and their birthday date in format mm-dd to a sqlite3 db via executing data.py.
In the main file, the programs checks if a friend has a birthday today using a function called birthday_checker () written in birthday_checker.py. 
If a friend has a birthday today, main.py sends a Whatsapp message (msg) to the friend using Selenium Chrome Webdriver. 

The program needs to be scheduled to run everyday at the same time. Scheduling can be done via another script or an external tool (e.g Windows Task Scheduler).

Enjoy!
God bless