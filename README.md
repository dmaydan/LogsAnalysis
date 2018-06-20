<h1>Logs Analysis Project</h1>
This is my submission for Udacity's Full Stack Web Developer Nanodegree's Logs Analysis Project. The task was to create a tool the analyzes a PostreSQL database of a news website and prints out reports. The report answers 3 questions:
<ol>
  <li>What are the most popular three articles of all time?</li>
  <li>Who are the most popular article authors of all time?</li>
  <li>On which days did more than 1% of requests lead to errors?</li>
</ol>
<h2>Setup</h2>
For this project, I used a Linux-based VM that gave me access to PostreSQL along with other software necessary for the project. 
<h3>VM Setup</h3>
<ol>
  <li>Install the platform package of VirtualBox https://www.virtualbox.org/wiki/Download_Old_Builds_5_1: VirtualBox is what actually runs the VM</li>
  <li>Install Vagrant https://www.vagrantup.com/downloads.html: Vagrant configures the VM and lets you share files between your host computer and the VM's filesystem</li>
  <li>Fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm. This is the VM configuration. All the work will be done in this directory.</li>
  <li>In terminal, change to this directory with <code>cd</code>. Then, <code>cd</code> into the vagrant folder.</li>
  <li>Run the command <code>vagrant up</code>. This tells Vagrant to download the Linux operating system, which can take a long time.</li>
  <li>Run the command <code>vagrant ssh</code> to log into the newly installed Linux VM.</li>
</ol>
<h3>Download the Data</h3>
<ol>
  <li>Download and unzip https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip.</li>
  <li>Put this file in the vagrant directory.</li>
  <li>To run the reporting tool you will need to load the news site's data into the local database news that has already been created for you. In the VM, <code>cd</code> into the vagrant subdirectory and run the command <code>psql -d news -f newsdata.sql</code>:
    <ul>
      <li><code>psql</code> — the PostgreSQL command line program</li>
      <li><code>-d news — connect</code> to the database named news which has been set up for you.</li>
      <li><code>-f newsdata.sql</code> — run the SQL statements in the file newsdata.sql that you just downloaded, creating tables and populating them with data.</li>
    </ul></li>
 </ol>
<h3>Install psycopg2</h3>
psycopg2 is the python library that allows python to work with PostreSQL. Simply run the command <code>pip3 install psycopg2</code>
<h2>Run</h2>
Everything is setup now. All you have to do is run <code>loganalysis.py</code> with python3: <code>python3 loganalysis.py</code>
<h2>Sample Output</h2>
```python
TOP THREE ARTICLES BY PAGE VIEWS
(1) "Candidate is jerk, alleges rival" with 338647 views
(2) "Bears love berries, alleges bear" with 253801 views
(3) "Bad things gone, say good people" with 170098 views
TOP THREE AUTHORS BY PAGE VIEWS
(1) "Ursula La Multa" with 507594 views
(2) "Rudolf von Treppenwitz" with 423457 views
(3) "Anonymous Contributor" with 170098 views
DAYS WITH MORE THAN 1% ERRORS
7/17/2016 -- 2.3% errors
```
