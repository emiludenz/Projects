--Users(name,address,phone,age,need)
drop table users;
create table users (
	name varchar(50) not null,
	address varchar(100) not null,
	phone varchar(16) not null,
	age smallint,
	need varchar(500) not null,
	appointment date,
	primary key (name)
);

start transaction;
insert into users values('Emil Bæk Henriksen', 'Buntmagervej 2,1mf','+4531160267',29,'Chips and dip',null);
insert into users values('Sune Loft', 'Not Buntmagervej 2,1mf','not +4531160267',null,'dulmeurt',null);
commit;