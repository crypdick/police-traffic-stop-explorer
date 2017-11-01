"""Backend for boilerplate sql queries using psycopg2

"""


import psycopg2


conn = psycopg2.connect(dbname='Open_Policing')
cur = conn.cursor()
"""
id,
stop_date,
stop_time, location_raw,
county_name, county_fips,
driver_gender, driver_age,
driver_race, violation,
search_conducted, search_type,
stop_outcome, is_arrested,
officer_id, officer_gender,
officer_age, officer_race,
officer_rank,
out_of_state
"""

query_by_county = ''
query_whole_state = ''

# Do a loop to append user specs to queries
for specs in user_specs:
    query_by_county += query_by_county + specs

# query_whole_state should be the same query without the GROUP BY
query_whole_state = query_by_county
query_by_county = query_by_county + ' GROUP BY county_name ORDER BY county_name;'
query_whole_state = query_whole_state + ';'

cur.execute(query_by_county)
counties_counts = cur.fetchall()

cur.execute(query_whole_state)

