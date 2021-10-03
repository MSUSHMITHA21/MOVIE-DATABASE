import sqlite3
conn=sqlite3.connect("movies.db")
c=conn.cursor()
c.execute("Create table favouritemovies1(name text varchar(20), actor text varchar(20), actress text varchar(20), director text varchar(20), year int(20))")
rows=[('Narappa', 'Venkatesh', 'priyamani', 'Srikanth addala', 2021),
       ('Mirchi' , 'Prabhas', 'Anushka', 'Koratala shiva', 2013),
      ('Bahubali', 'Prabhas', 'Anushka', 'Rajamouli', '2017')]
c.execute("select * from favouritemovies1")
rec=c.fetchall()
print(rec)
conn.commit()
conn.close()
