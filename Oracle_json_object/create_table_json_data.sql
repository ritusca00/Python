create table json_data
(
 id NUMBER generated always as identity,
 name varchar2(4000),
 workday date,
 hours   number
);


insert into JSON_DATA (NAME, WORKDAY, HOURS)
values ('Kis István', to_date('06-02-2019', 'dd-mm-yyyy'), 8);

insert into JSON_DATA (NAME, WORKDAY, HOURS)
values ('Kis Péter', to_date('06-02-2019', 'dd-mm-yyyy'), 7);

insert into JSON_DATA (NAME, WORKDAY, HOURS)
values ('Kis Andor', to_date('06-02-2019', 'dd-mm-yyyy'), 8);

insert into JSON_DATA (NAME, WORKDAY, HOURS)
values ('Kis János', to_date('06-02-2019', 'dd-mm-yyyy'), 7);

insert into JSON_DATA (NAME, WORKDAY, HOURS)
values ('Kis Béla', to_date('06-02-2019', 'dd-mm-yyyy'), 2);

insert into JSON_DATA (NAME, WORKDAY, HOURS)
values ('Kis István', to_date('05-02-2019', 'dd-mm-yyyy'), 8);

insert into JSON_DATA (NAME, WORKDAY, HOURS)
values ('Kis Péter', to_date('05-02-2019', 'dd-mm-yyyy'), 7);

insert into JSON_DATA (NAME, WORKDAY, HOURS)
values ('Kis Andor', to_date('05-02-2019', 'dd-mm-yyyy'), 8);

insert into JSON_DATA (NAME, WORKDAY, HOURS)
values ('Kis János', to_date('05-02-2019', 'dd-mm-yyyy'), 7);

insert into JSON_DATA (NAME, WORKDAY, HOURS)
values ('Kis Béla', to_date('05-02-2019', 'dd-mm-yyyy'), 2);

