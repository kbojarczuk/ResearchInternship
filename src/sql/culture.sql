-- culture.sql

USE culture;

-- CREATE TABLE


-- Get the data into CSV, use python
-- Check out openpyxl (http://www.python-excel.org/)
-- Write python scripts to write the institutions.csv file

-- Importing  Data
-- http://dev.mysql.com/doc/refman/5.7/en/load-data.html
-- load data infile 'institutions.csv' into table institutions FIELDS TERMINATED BY ',' ;

-- OR use mysqlimport
-- http://dev.mysql.com/doc/refman/5.7/en/mysqlimport.html


CREATE TABLE Institution(
id INTEGER,
name VARCHAR(70) NOT NULL,
alt_name VARCHAR(150),
area VARCHAR(30),
region VARCHAR(30),
category VARCHAR(30),
subcategory VARCHAR(20),
country VARCHAR(20),
local_authority VARCHAR(40),
website VARCHAR(100),
lat REAL,
lng REAL,
local_ecode INTEGER,
PRIMARY KEY(id),
FOREIGN KEY(local_ecode) REFERENCES Local_auth(ecode)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/ac/inst.csv' INTO TABLE Institution FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 

CREATE TABLE Finance(
year VARCHAR(20),
prog VARCHAR(20),
source VARCHAR(20),
funds VARCHAR(30),
notes VARCHAR(250),
institution_id INTEGER,
PRIMARY KEY(year, prog,institution_id),
FOREIGN KEY(institution_id) REFERENCES Institution(id)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/ac/funds1718.csv' INTO TABLE Finance FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/ac/funds1617.csv' INTO TABLE Finance FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/ac/funds1516.csv' INTO TABLE Finance FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/ac/funds1415.csv' INTO TABLE Finance FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/ac/funds1314.csv' INTO TABLE Finance FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/ac/funds1213.csv' INTO TABLE Finance FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
--Cannot add or update a child row: a foreign key constraint fails (`culture`.`Finance`, CONSTRAINT `Finance_ibfk_1` FOREIGN KEY (`institution_name`) REFERENCES `Institution` (`name`)) |

CREATE TABLE Grants(
id INTEGER NOT NULL AUTO_INCREMENT,
year INTEGER,
name VARCHAR(100),
source VARCHAR(30),
prog VARCHAR(40),
heading VARCHAR(50),
funds REAL,
descr TEXT,
artform VARCHAR(30),
local VARCHAR(30),
reg VARCHAR(40),
cons VARCHAR(50),
ward VARCHAR(70),
PRIMARY KEY(id)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/ac/grants.csv' INTO TABLE Grants FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
 
source, prog, heading, artform
CREATE TABLE Tpart_freq(
type VARCHAR(20),
year VARCHAR(20),
freq VARCHAR(50),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, freq)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/freq_a.csv' INTO TABLE Tpart_freq FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/freq_m.csv' INTO TABLE Tpart_freq FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';  

CREATE TABLE Tpart_reason(
type VARCHAR(20),
year VARCHAR(20),
reason VARCHAR(70),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, reason)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/reason_m.csv' INTO TABLE Tpart_reason FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';  
CREATE TABLE Tpart_index(
type VARCHAR(20),
year VARCHAR(20),
index_depr VARCHAR(50),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, index_depr)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/index_a.csv' INTO TABLE Tpart_index FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/index_m.csv' INTO TABLE Tpart_index FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 

CREATE TABLE Tpart_reg(
type VARCHAR(20),
year VARCHAR(20),
region VARCHAR(30),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, region)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/reg_a.csv' INTO TABLE Tpart_reg FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/reg_m.csv' INTO TABLE Tpart_reg FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
CREATE TABLE Tpart_type(
type VARCHAR(20),
year VARCHAR(20),
type_area VARCHAR(10),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, type_area)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/type_a.csv' INTO TABLE Tpart_type FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/type_m.csv' INTO TABLE Tpart_type FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
CREATE TABLE Tpart_ACORN(
type VARCHAR(20),
year VARCHAR(20),
ACORN VARCHAR(30),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, ACORN)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/ACORN_a.csv' INTO TABLE Tpart_ACORN FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/ACORN_m.csv' INTO TABLE Tpart_ACORN FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 

CREATE TABLE Tpart_sex(
type VARCHAR(20),
year VARCHAR(20),
sex VARCHAR(10),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, sex)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/sex_a.csv' INTO TABLE Tpart_sex FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/sex_m.csv' INTO TABLE Tpart_sex FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
CREATE TABLE Tpart_ns(
type VARCHAR(20),
year VARCHAR(20),
ns VARCHAR(30),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, ns)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/ns_a.csv' INTO TABLE Tpart_ns FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/ns_m.csv' INTO TABLE Tpart_ns FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Tpart_emp(
type VARCHAR(20),
year VARCHAR(20),
emp VARCHAR(20),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, emp)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/emp_a.csv' INTO TABLE Tpart_emp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/emp_m.csv' INTO TABLE Tpart_emp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
CREATE TABLE Tpart_tenure(
type VARCHAR(20),
year VARCHAR(20),
tenure VARCHAR(30),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, tenure)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/tenure_a.csv' INTO TABLE Tpart_tenure FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/tenure_m.csv' INTO TABLE Tpart_tenure FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
CREATE TABLE Tpart_eth(
type VARCHAR(20),
year VARCHAR(20),
eth VARCHAR(30),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, eth)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/eth_a.csv' INTO TABLE Tpart_eth FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/eth_m.csv' INTO TABLE Tpart_eth FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
CREATE TABLE Tpart_rel(
type VARCHAR(20),
year VARCHAR(20),
rel VARCHAR(30),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, rel)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/rel_a.csv' INTO TABLE Tpart_rel FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/rel_m.csv' INTO TABLE Tpart_rel FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
CREATE TABLE Tpart_disab(
type VARCHAR(20),
year VARCHAR(20),
disab VARCHAR(30),
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, disab)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/disab_a.csv' INTO TABLE Tpart_disab FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/disab_m.csv' INTO TABLE Tpart_disab FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
CREATE TABLE Tpart_age(
type VARCHAR(20),
year VARCHAR(20),
age_from INTEGER,
age_to INTEGER,
prg REAL,
range_resp REAL,
respondents INTEGER,
PRIMARY KEY(type, year, age_from)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/age_a.csv' INTO TABLE Tpart_age FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/tpart/age_m.csv' INTO TABLE Tpart_age FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Local_auth(
ecode INTEGER,
ons VARCHAR(20),
name VARCHAR(120) NOT NULL,
reg VARCHAR(20),
class VARCHAR(20),
PRIMARY KEY(ecode)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/local/local_list.csv' INTO TABLE Local_auth FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/local/local_list2.csv' INTO TABLE Local_auth FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
INSERT INTO Local_auth VALUES('1','','Cardiff','','');
INSERT INTO Local_auth VALUES('2','','Powys','','');

CREATE TABLE Local_auth_budget(
type VARCHAR(30),
year VARCHAR(20),
budget REAL,
local_ecode INTEGER,
PRIMARY KEY(type, year,local_ecode),
FOREIGN KEY(local_ecode) REFERENCES Local_auth(ecode)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/local/local_budget1213.csv' INTO TABLE Local_auth_budget FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/local/local_budget1314.csv' INTO TABLE Local_auth_budget FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/local/local_budget1415.csv' INTO TABLE Local_auth_budget FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
 
CREATE TABLE Local_auth_exp(
type VARCHAR(50),
year VARCHAR(20),
expenditure REAL,
local_ecode INTEGER,
PRIMARY KEY(type, year,local_ecode),
FOREIGN KEY(local_ecode) REFERENCES Local_auth(ecode)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/local/local12.csv' INTO TABLE Local_auth_exp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/local/local13.csv' INTO TABLE Local_auth_exp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'; 
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/local/local14.csv' INTO TABLE Local_auth_exp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/local/local15.csv' INTO TABLE Local_auth_exp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_reg_emp(
year VARCHAR(20),
area VARCHAR(50),
sector VARCHAR(50),
prg REAL,
PRIMARY KEY(year, area, sector)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint1.csv' INTO TABLE Blueprint_reg_emp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_reg_wages(
year VARCHAR(20),
area VARCHAR(50),
wage REAL,
PRIMARY KEY(year, area)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint_wages.csv' INTO TABLE Blueprint_reg_wages FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_reg_div(
year VARCHAR(20),
diversity VARCHAR(50),
type VARCHAR(50),
area VARCHAR(50),
prg REAL,
PRIMARY KEY(year, diversity, type, area)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint3.csv' INTO TABLE Blueprint_reg_div FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';


CREATE TABLE Blueprint_reg_qual (
year varchar(20),
area varchar(50),
qual VARCHAR(50),
creative_distr REAL,
distr REAL;
PRIMARY KEY (year,area, qual)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint8.csv' INTO TABLE Blueprint_reg_qual FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';


CREATE TABLE Blueprint_reg_GVA (
year varchar(20),
area varchar(50),
GVA REAL,
PRIMARY KEY (year,area)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint9.csv' INTO TABLE Blueprint_reg_GVA FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_reg_sectors (
year varchar(20),
area varchar(50),
sector varchar(50),
GVA REAL,
PRIMARY KEY (year,area,sector)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint9a.csv' INTO TABLE Blueprint_reg_sectors FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';


CREATE TABLE Blueprint_reg_business (
year varchar(20),
area varchar(50),
bus_size VARCHAR(20),
creative_distr REAL,
distr REAL,
PRIMARY KEY (year,area, bus_size)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint10.csv' INTO TABLE Blueprint_reg_business FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_reg_age (
year varchar(20),
area varchar(50),
age_from INTEGER,
age_to INTEGER,
creative_distr REAL,
distr REAL,
PRIMARY KEY (year,area,age_from)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint2.csv' INTO TABLE Blueprint_reg_age FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_type_emp(
year VARCHAR(20),
sector VARCHAR(50),
subsector VARCHAR(50),
prg REAL,
PRIMARY KEY(year, sector, subsector)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint1type.csv' INTO TABLE Blueprint_type_emp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_type_wages(
year VARCHAR(20),
sector VARCHAR(50),
wage REAL,
PRIMARY KEY(year, sector)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint_wages_type.csv' INTO TABLE Blueprint_type_wages FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_type_div(
year VARCHAR(20),
sector VARCHAR(50),
diversity VARCHAR(50),
prg REAL,
PRIMARY KEY(year, sector, diversity)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint3type.csv' INTO TABLE Blueprint_type_div FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_type_qual (
year varchar(20),
sector varchar(50),
qual VARCHAR(50),
prg REAL,
PRIMARY KEY (year,sector, qual)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint8type.csv' INTO TABLE Blueprint_type_qual FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_type_GVA (
year varchar(20),
sector varchar(50),
subsector varchar(50),
GVA REAL,
PRIMARY KEY (year,sector, subsector)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint9type.csv' INTO TABLE Blueprint_type_GVA FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_type_business (
year VARCHAR(20),
sector VARCHAR(50),
bus_size VARCHAR(20),
prg REAL,
PRIMARY KEY (year,sector, bus_size)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint10.csv' INTO TABLE Blueprint_type_business FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

CREATE TABLE Blueprint_type_age (
year varchar(20),
sector varchar(50),
age_from INTEGER,
age_to INTEGER,
prg REAL,
PRIMARY KEY (year,sector,age_from)
);
LOAD DATA LOCAL INFILE '/proj/melba/culture/data/blueprint/blueprint2type.csv' INTO TABLE Blueprint_type_age FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

