use proyectNasa;

create table dataSensor(
	id int auto_increment not null,
    humidity int not null,
    temp_c float not null,
    temp_f float not null,
    constraint pk_data_sensor primary key(id)
);