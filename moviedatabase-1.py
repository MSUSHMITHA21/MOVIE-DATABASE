import sqlite3
conn=sqlite3.connect("movies.db")
c=conn.cursor()
c.execute("Create table favmov12(name text varchar(30), actor text varchar(30), actress text varchar(30), director text varchar(30), villain text varchar
(30), year int(30))")
rows=[('Lovestory', 'Naga Chaitanya', 'Sai Pallavi', 'Shkehar Kammula', 'Shankar', 2021),
       ('Gabbar Singh' , 'Pawan Kalyan', 'Sruthi Hasan', 'Harish Shankar', 'Narayana', 2012),
      ('Majnu', 'Nani', 'Anu Emmanuel', 'Virinchi Varma', 'Vamsi Krishna', '2016')]
c.execute("select * from favmov12")
rec=c.fetchall()
print(rec)
conn.commit()
conn.close()
