CREATE SCHEMA IF NOT EXISTS "public";

CREATE  TABLE r3c_database."public".data ( 
	horodatage           timestamp DEFAULT CURRENT_TIMESTAMP   ,
	device_id            bigint NOT NULL   ,
	battery              integer    ,
	temperature          float    ,
	humidity             float
);

CREATE  TABLE r3c_database."public".device_location ( 
	device_id            bigint NOT NULL   ,
	location_id          integer
);

CREATE  TABLE r3c_database."public".locations ( 
	location_id            integer NOT NULL   ,
	location_name          varchar NOT NULL
);

CREATE  TABLE r3c_database."public".device_surname ( 
	device_id            bigint NOT NULL  ,
	device_name          varchar NOT NULL
);


\c r3c_database

CREATE USER r3c_user WITH LOGIN ENCRYPTED PASSWORD 'EfJ7K&k_kSAA';

GRANT CONNECT ON DATABASE r3c_database TO r3c_user;
GRANT USAGE ON SCHEMA public TO r3c_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO r3c_user;
GRANT INSERT ON ALL TABLES IN SCHEMA public TO r3c_user;

CREATE USER grafanauser WITH LOGIN ENCRYPTED PASSWORD 'LsKs75&_IsdK';

GRANT CONNECT ON DATABASE r3c_database TO grafanauser;
GRANT USAGE ON SCHEMA public TO grafanauser;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO grafanauser;
