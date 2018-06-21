#!/usr/bin/env python3.
import psycopg2
import datetime
conn = psycopg2.connect("dbname=news")

cursor = conn.cursor()

cursor.execute("""select articles.title, count(log.path)
                as num from articles left join
                log on log.path like concat('/article/', articles.slug)
                where log.path like '/article%' and log.method = 'GET'
                and log.status = '200 OK' group by articles.title order
                by num desc limit 3;""")

results1 = cursor.fetchall()

counter1 = 1

print("TOP THREE ARTICLES BY PAGE VIEWS")

for row in results1:
    print(
        '(' + str(counter1) + ') "' + row[0] +
        '" with ' + str(row[1]) + ' views')
    counter1 += 1

cursor.execute("""select authors.name, count(log.path) as num
                from articles left join authors
                on articles.author = authors.id left join log on
                log.path like concat('/article/', articles.slug)
                where log.path like '/article%' and log.method =
                'GET' and log.status = '200 OK' group by authors.name
                order by num desc limit 3;""")

results2 = cursor.fetchall()

counter2 = 1

print("TOP THREE AUTHORS BY PAGE VIEWS")

for row in results2:
    print(
        '(' + str(counter2) + ') "' +
        row[0] + '" with ' + str(row[1]) + ' views')
    counter2 += 1

cursor.execute("""select date, error, total from
                (select CAST(time AS date)
                as date, count(status) filter
                (where status like '4%' or status like '5%')
                as error, count(status) as total from log group by date)
                as statuscodetable where CAST(error AS float) / CAST(total
                AS float) * 100 > 1;""")


results3 = cursor.fetchall()

print("DAYS WITH MORE THAN 1% ERRORS")

for row in results3:
    percent = str(round((float(row[1])/float(row[2])*100), 1))
    print(
        str(row[0].strftime('%B')) + ' ' + str(row[0].day) +
        ', ' + str(row[0].year) + ' -- ' + percent + '% errors')

conn.close()
