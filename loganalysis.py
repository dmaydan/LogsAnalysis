import psycopg2
import datetime
conn = psycopg2.connect("dbname=news")

cursor = conn.cursor()

cursor.execute("select articles.title, count(log.path) as num from articles left join log on log.path like concat('/article/', articles.slug) where log.path like '/article%' and log.method = 'GET' and log.status = '200 OK' group by articles.title order by num desc limit 3;")

results1 = cursor.fetchall()

for row in results1:
	print("Article: " + row[0] + ' - ' + str(row[1]))

cursor.execute("select authors.name, count(log.path) as num from articles left join authors on articles.author = authors.id left join log on log.path like concat('/article/', articles.slug) where log.path like '/article%' and log.method = 'GET' and log.status = '200 OK' group by authors.name order by num desc;")

results2 = cursor.fetchall()

for row in results2:
	print("Author: " + row[0] + ' - ' + str(row[1]))

cursor.execute("select date, error, total from (select CAST(time AS date) as date, count(status) filter (where status like '4%' or status like '5%') as error, count(status) as total from log group by date) as statuscodetable where CAST(error AS float) / CAST(total AS float) * 100 > 1;")


results3 = cursor.fetchall()

for row in results3:
	percent = float(row[1])/float(row[2])*100
	print(str(row[0]) + ' - ' + str(percent) + ' percent')

conn.close()

