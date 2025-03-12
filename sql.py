import sqlite3

connection=sqlite3.connect("student.db")

# create a cursor object to insert records, create table and retrieve
cursor=connection.cursor()

table_info="""
create table student(
    name varchar(25),
    class varchar(25),
    section varchar(25),
    marks int
);
"""

cursor.execute(table_info)

cursor.execute('''insert into student values ('Krish', 'Data Science', 'A', 90)''') 
cursor.execute('''insert into student values ('Darius', 'Data Science', 'B', 100)''') 
cursor.execute('''insert into student values ('Sudhanshu', 'Devops', 'C', 86)''') 
cursor.execute('''insert into student values ('Vikash', 'Data Science', 'C', 50)''') 
cursor.execute('''insert into student values ('Sush', 'Devops', 'C', 35)''') 

print("the inserted records are")
data=cursor.execute('''select * from student''')

for row in data:
    print(row)

connection.commit()
connection.close()