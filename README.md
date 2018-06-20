# LogsAnalysis
This is my submission for Udacity's Full Stack Web Developer Nanodegree's Log Analysis Project. Postresql is used to analyze a database that contains server logs along with other information.
## Install
I used a VM to run this application. To do this, install vagrant, run commands <code>vagrant up</code> <code>vagrant ssh</code> Then, change directories inside the vm shell to the vagrant directory that is shared with the regular os. 
##Setup
Clone this repo. On your machine, create a psql database called news in the repo. Then, run the psql command <code>psql -d news -f newsdata.sql</code>, which connects you to the news database and runs the SQL statements in the newsdata.sql file. Finally, you can run the loganalysis.py file with python3.
