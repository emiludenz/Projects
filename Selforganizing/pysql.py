import sqlite3
connection = sqlite3.connect("users.db")
cursor = connection.cursor()
cursor.execute("""DROP TABLE users;""")

sql_command = """
create table users (
	name varchar(50) not null,
	address varchar(100) not null,
	phone varchar(16) not null,
	age smallint,
	need varchar(500) not null,
	appointment date,
	primary key (name)
);"""
cursor.execute(sql_command)
sql_command = """
insert into users values('Emil Bæk Henriksen', 'Buntmagervej 2,1mf','+4531160267',29,'Chips and dip',null);"""
cursor.execute(sql_command)
sql_command = """
insert into users values('Sune Loft', 'Not Buntmagervej 2,1mf','not +4531160267',null,'dulmeurt',null);"""
cursor.execute(sql_command)
cursor.execute("SELECT * FROM users") 
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)