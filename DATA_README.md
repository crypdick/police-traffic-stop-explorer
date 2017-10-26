Original columns: id,state,stop_date,stop_time,location_raw,county_name,county_fips,fine_grained_location,police_department,driver_gender,driver_age_raw,driver_age,driver_race_raw,driver_race,violation_raw,violation,search_conducted,search_type_raw,search_type,contraband_found,stop_outcome,is_arrested,officer_id,officer_gender,officer_age,officer_race,officer_rank,out_of_state

cols to skip:
2 state
8 fine_grained_location (mostly empty)
9 police_department (empty)
11 driver_age_raw (dupe)
13 driver_race_raw (dupe)
15 violation_raw (dupe)
18 search_type_raw (dupe)
20 contraband_found (empty)

result:
id,state,stop_date,stop_time,location_raw,county_name,county_fips,driver_gender,driver_age,driver_race,violation,search_conducted,search_type,stop_outcome,is_arrested,officer_id,officer_gender,officer_age,officer_race,officer_rank,out_of_state


CREATE TABLE FL_stops (
    id TEXT PRIMARY KEY,
    stop_date DATE,
    stop_time TIME,
    location_raw TEXT,
    county_name  TEXT,
    county_fips INTEGER,
    driver_gender CHAR(1),
    driver_age INT,
    driver_race TEXT,
    violation TEXT,
    search_conducted BOOL,
    search_type TEXT,
    stop_outcome TEXT,
    is_arrested BOOL,
    officer_id INT,
    officer_gender CHAR(1),
    officer_age INT,
    officer_race TEXT,
    officer_rank TEXT,
    out_of_state BOOL
);

\copy FL_stops (id,stop_date,stop_time,location_raw,county_name,county_fips,driver_gender,driver_age,driver_race,violation,search_conducted,search_type,stop_outcome,is_arrested,officer_id,officer_gender,officer_age,officer_race,officer_rank,out_of_state) FROM 'FL-clean.csv' DELIMITERS ',' CSV HEADER;
